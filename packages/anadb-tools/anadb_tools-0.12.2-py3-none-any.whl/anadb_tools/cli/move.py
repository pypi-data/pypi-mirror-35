"""
anadb-move
==========

Move an analytics database from one server to another.

"""
import os
from os import path
import random
import subprocess
import tempfile

from anadb_tools import anabroker
from anadb_tools import anadb
from anadb_tools import appdb
from anadb_tools import common
from anadb_tools import database

LOGGER = common.get_logger()


def execute(args):
    """Move a customer's analytics database from its existing location to
    a new server.

    :param argparse.namespace args: The parsed cli arguments

    """
    dest = get_dest_server(args)

    # Dont allow metrics to come in while the account is being moved
    anadb.deactivate(args, args.account)

    # Figure out where we are moving the account from
    source = anadb.lookup(args, args.account)

    # Create the destination database without ana_template
    anadb.create(args, dest['hostname'], dest['port'], args.account, False)

    # Migrate the data
    if not migrate_data(args, source, dest):
        LOGGER.critical('Migration of data failed, exiting')
        return

    # Backup the original database
    backup_path = database.backup(args,
                                  source['hostname'],
                                  source['port'],
                                  source['dbname'])

    appdb.add_note(args, args.account, 'Analytics Backup',
                   'Customer analytics database backed up to {}'.format(
                       backup_path))

    # Remove the original
    database.drop(args, source['hostname'], source['port'], source['dbname'])

    # Assign and activate the host in the new location
    anadb.assign(args, args.account, dest['hostname'])
    anadb.activate(args, args.account)

    appdb.add_note(args, args.account, 'Analytics Database Move',
                   'Analytics database moved from {} to {}'.format(
                       source['hostname'], dest['hostname']))
    LOGGER.info('Analytics database for account %s moved to %s',
                args.account, dest['hostname'])


def get_dest_server(args):
    """Get the connection information for the destination server. The
    destination server is either explicitly stated or it is chosen from the
    available servers at random.

    :param argparse.namespace args: The parsed cli arguments
    :rtype: dict

    """
    if args.host:
        connection = anabroker.connect(args)
        cursor = connection.cursor()
        cursor.execute('SELECT hostname, port '
                       '  FROM db_nodes '
                       ' WHERE hostname=%(hostname)s', {'hostname': args.host})
        if not cursor.rowcount:
            raise ValueError('{} not found'.format(args.host))
        return cursor.fetchone()
    elif args.random:
        servers = anabroker.servers(args, True, True)
        return servers[random.randint(0, len(servers) - 1)]


def migrate_data(args, source, dest):
    """Perform the dump and load of the data from the source database to the
    destination database.

    :param argparse.namespace args: The parsed cli arguments
    :param dict source: The source connection information
    :param dict dest: The destination connection information
    :return: Success or failure
    :rtype: bool

    """
    LOGGER.info('Moving account %i from %s:%i to %s:%i', args.account,
                source['hostname'], source['port'],
                dest['hostname'], dest['port'])

    filename = path.join(tempfile.gettempdir(),
                         'ana_{}_{}.dump'.format(args.account,
                                                 source['hostname']))
    command = ['pg_dump',
               '-h', source['hostname'],
               '-p', str(source['port']),
               '-d', 'ana_{}'.format(args.account),
               '-U', args.username,
               '--exclude-table-data=ana.message_types',
               '-Fc', '-x', '-v', '-a', '-f', filename,
               '--serializable-deferrable',
               '--no-tablespaces']
    if args.role:
        command.append('--role')
        command.append(args.role)

    dump = subprocess.Popen(command,
                            stderr=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    LOGGER.debug('Waiting for pg_dump of %s to complete', source['hostname'])
    dump.wait()
    if dump.returncode:
        _stdout, stderr = dump.communicate()
        LOGGER.error('pg_dump of ana_%i failed (%s): %s',
                     args.account, dump.returncode, stderr)
        return False

    restore = subprocess.Popen(['pg_restore',
                                '-h', dest['hostname'],
                                '-p', str(dest['port']),
                                '-U', args.username,
                                '-Fc', '-a', '-e', '-v',
                                '-d', 'ana_{}'.format(args.account),
                                filename],
                               stdin=dump.stdout,
                               stderr=subprocess.PIPE,
                               stdout=subprocess.PIPE)

    LOGGER.debug('Waiting for psql restore to %s to complete',
                 dest['hostname'])
    restore.wait()
    _stdout, stderr = restore.communicate()

    # Remove the dump temp file
    os.unlink(filename)

    if restore.returncode:
        LOGGER.error('Error restoring ana_%i to %s (%s): %s', args.account,
                     dest['hostname'], restore.returncode, stderr)
        return False

    return True


def main():
    parser = common.argument_parser('Move an analytics database from one '
                                    'server to another')
    parser.add_argument('-a', '--account', help='Account to move', type=int,
                        action='store', required=True)
    parser.add_argument('-h', '--host', action='store',
                        help='The analytics server to move the account to')
    parser.add_argument('-r', '--random', action='store_true',
                        help='Assign the new server at random')
    database.add_backup_arguments(parser)
    args = common.parse_arguments(parser)
    if not args.host and not args.random:
        common.exit_application('You must specify a host or random assignment',
                                1)
    elif args.host and args.random:
        common.exit_application('You can not specify both a host and random '
                                'assignment', 2)
    else:
        execute(args)


if __name__ == '__main__':
    main()
