"""
Common PostgreSQL database functions

"""
import datetime
import getpass
import logging
import os
from os import path
import subprocess
import tempfile

import boto3
from psycopg2 import extras
import pgpasslib
import psycopg2

from anadb_tools import exceptions


LOGGER = logging.getLogger(__name__)

S3_PATH = 'backup/anadb/%(date)s/%(hostname)s/%(filename)s'


def add_backup_arguments(parser):
    """Add CLI arguments required for this module.

    :param argparse.ArgumentParser parser: The argument parser

    """
    parser.add_argument('-b', '--s3-bucket', type=str, action='store',
                        help='The S3 bucket to upload the database backup to. '
                             'Default: com-aweber-dba',
                        default='com-aweber-dba')


def backup(args, hostname, port, dbname):
    """Backup the specified database to Amazon S3

    :param argparse.namespace args: The CLI arguments
    :param str hostname: The hostname to backup the database from
    :param int port: The port to connect to the database on
    :param str dbname: The database to backup
    :rtype: str

    """
    backup_path = _backup_file(dbname)
    LOGGER.debug('Backing up to %s', backup_path)
    dump(args, hostname, port, dbname, backup_path)
    upload_path = _upload_to_s3(args, backup_path, hostname)
    os.unlink(backup_path)
    return upload_path


def drop(args, hostname, port, db_name):
    """Drop the database from the anadb server.

    :param argparse.namespace args: The CLI arguments
    :param str hostname: The hostname to dump the database from
    :param int port: The port to connect on
    :param str db_name: The database to drop

    """
    LOGGER.debug('Dropping %s from %s:%s', db_name, hostname, port)
    subprocess.check_call(_drop_command(args, hostname, port, db_name))


def dump(args, hostname, port, dbname, output_file):
    """Return the pg_dump command to run to backup the database.

    :param argparse.namespace args: The CLI arguments
    :param str hostname: The hostname to dump the database from
    :param int port: The port to connect on
    :param str dbname: The database to backup
    :param str output_file: The filename to backup to

    """
    LOGGER.debug("Dumping %s on %s:%s to %s",
                 dbname, hostname, port, output_file)
    subprocess.check_call(_dump_command(args, hostname, port, dbname,
                                        output_file))


def connect(host, port, dbname, username, role=None, prompt=False,
            password_prompt=None, autocommit=True):
    """Returns a psycopg2 :class:`~psycopg2.extensions.connection` for
    the specified arguments, with autocommit turned on.

    :param str host: The database server host
    :param int port: The database server port
    :param str dbname: The database to connect to
    :param str username: The username to connect as
    :param bool prompt: Prompt if the password can't be loaded from ``.pgpass``
    :param str role: The role to assume once connected
    :param str password_prompt: The password prompt to use if needed
    :param bool autocommit: Enable/Disable autocommit
    :rtype: :class:`~psycopg2.extensions.connection`

    """
    # Try and get the password from ~/.pgpass
    try:
        password = pgpasslib.getpass(host, port, dbname, username)
    except pgpasslib.FileNotFound:
        password = None

    # If prompt is true and we still don't have a password, prompt for it
    if not password and prompt:
        password = getpass.getpass(password_prompt or
                                   '{} Password: '.format(host))

    LOGGER.debug('Connecting to %s at %s:%s as %s',
                 dbname, host, port, username)
    try:
        conn = psycopg2.connect(host=host,
                                port=port,
                                user=username,
                                password=password,
                                database=dbname,
                                cursor_factory=extras.RealDictCursor)
    except psycopg2.OperationalError as error:
        raise exceptions.ConnectionError(str(error))
    if autocommit:
        conn.autocommit = True
    if role:
        set_role(conn, role)
    return conn


def set_role(conn, name):
    """Set the specified role on the database connection

    :param psycopg2.extensions.connection conn: The PostgreSQL connection
    :param str name: The role to set

    """
    cursor = conn.cursor()
    cursor.execute('SET role=%(name)s;', {'name': name})
    cursor.close()


def _backup_file(db_name):
    """Return the full path to use when creating the backup.

    :param str db_name: The database name

    """
    return '{}/{}.dump'.format(tempfile.gettempdir(), db_name)


def _drop_command(args, hostname, port, db_name):
    """Return the dropdb command to run to backup the database.

    :param argparse.namespace args: The CLI arguments
    :param str hostname: The hostname to dump the database from
    :param int port: The port to connect on
    :param str db_name: The database to backup
    :rtype: list

    """
    return ['dropdb', '-U', args.username, '-h', hostname, '-p',
            str(port), db_name]


def _dump_command(args, hostname, port, dbname, output_file):
    """Return the pg_dump command to run to backup the database.

    :param argparse.namespace args: The CLI arguments
    :param str hostname: The hostname to dump the database from
    :param int port: The port to connect on
    :param str dbname: The database to backup
    :param str output_file: The filename to backup to
    :rtype: list

    """
    command = ['pg_dump', '-U', args.username, '-h', hostname, '-p',
               str(port), '-d', dbname, '-Fc', '--no-tablespaces', '-O',
               '-Z', '9', '-f', output_file]
    if args.role:
        command += ['--role', args.role]
    LOGGER.debug('Dump command: %r', ' '.join(command))
    return command


def _upload_to_s3(args, backup_path, hostname):
    """Upload the backup file to S3

    :param argparse.namespace args: The CLI arguments
    :param str backup_path: The full path to the backup file
    :param str hostname: The hostname the backup was taken from
    :rtype: upload_path

    """
    stat = os.stat(backup_path)
    upload_path = S3_PATH % {'date': datetime.date.today().isoformat(),
                             'hostname': hostname,
                             'filename': path.basename(backup_path)}
    LOGGER.debug('Uploading the %i byte backup to s3://%s%s',
                 stat.st_size, args.s3_bucket, upload_path)
    s3 = boto3.client('s3')
    s3.upload_file(backup_path, args.s3_bucket, upload_path)
    LOGGER.debug('Upload of %s complete', backup_path)
    return 's3://{}/{}'.format(args.s3_bucket, upload_path)
