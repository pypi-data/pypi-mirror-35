"""
Account Specific Analytics Database Functions


"""
import logging
import os

import psycopg2

from anadb_tools import anabroker
from anadb_tools import database
from anadb_tools import exceptions
from anadb_tools import redcache


LOGGER = logging.getLogger(__name__)

INSERT_ASSIGNMENT = """\
INSERT INTO db_node_assignments
       (a_id, db_node_id, db_name)
VALUES (%(a_id)s,
        (SELECT id FROM db_nodes WHERE hostname=%(hostname)s),
        %(dbname)s);"""

LOOKUP_ASSIGNMENT = """\
SELECT a_id, hostname, port, dbname, active, external_rollups
  FROM ana_db_locations WHERE a_id = %(a_id)s;"""

REMOVE_ASSIGNMENT = "DELETE FROM db_node_assignments WHERE a_id = %(a_id)s;"

TOGGLE_ACCOUNT_ACTIVE = """\
UPDATE db_node_assignments SET active = %(active)s WHERE a_id = %(a_id)s;"""

UPDATE_ASSIGNMENT = """\
UPDATE db_node_assignments
   SET db_node_id = (SELECT id FROM db_nodes WHERE hostname=%(hostname)s)
 WHERE a_id = %(a_id)s;"""


def activate(args, account):
    """Activate the node in anabroker

    :param argparse.namespace args: The parsed cli arguments
    :param int account: The account to deactivate

    """
    cursor = anabroker.cursor(args)
    LOGGER.debug('Activating account %i in anabroker', account)
    cursor.execute(TOGGLE_ACCOUNT_ACTIVE, {'a_id': account, 'active': True})
    cursor.close()
    redcache.clear_assignments(account)


def assign(args, account, hostname):
    """Assign the specified account to the specified database server in
    the analytics broker.

    :param argparse.namespace args: The parsed cli arguments
    :param int account: The account to deactivate
    :param str hostname: The database server to assign the account to
    :return:

    """
    cursor = anabroker.cursor(args)
    try:
        LOGGER.debug('Inserting database assignment for %s on %s',
                     account, hostname)
        cursor.execute(INSERT_ASSIGNMENT, {'a_id': account,
                                           'hostname': hostname,
                                           'dbname': 'ana_{}'.format(account)})
    except psycopg2.IntegrityError:
        LOGGER.debug('Assignment exists, updating %s to be on %s',
                     account, hostname)
        cursor.execute(UPDATE_ASSIGNMENT, {'a_id': account,
                                           'hostname': hostname})
    redcache.clear_assignments(account)


def connect(args, account, autocommit=True, allow_inactive=False):
    """Returns a psycopg2 :class:`~psycopg2.extensions.connection` for
    the specified account, in autocommit mode.

    :param argparse.namespace args: The parsed cli arguments
    :param int account: The customer's account ID to connect for
    :param bool autocommit: Enable/Disable autocommit
    :param bool allow_inactive: Allow connections to inactive databases
    :rtype: :class:`~psycopg2.extensions.connection`
    :raises: InactiveAnalyticsDatabase
    :raises: NoAnalyticsDatabase

    """
    params = lookup(args, account)
    if not allow_inactive and not params['active']:
        raise exceptions.InactiveAnalyticsDatabase
    return database.connect(params['hostname'],
                            params['port'],
                            params['dbname'],
                            os.environ.get('ANADB_USER', args.username),
                            args.role,
                            args.password,
                            'Analytics Database Password: ',
                            autocommit)


def create(args, hostname, port, account, no_template=False):
    """Create an analytics database

    :param argparse.namespace args: The parsed cli arguments
    :param str hostname: The host to create the database on
    :param int port: The port to connect on when connecting to the server
    :param int account: The account to create the database for
    :param bool no_template: Don't use ana_template as a base

    """
    LOGGER.info('Creating ana_%s on %s:%s', account, hostname, port)
    conn = database.connect(hostname, port, 'postgres', args.username,
                            args.role, args.password, True)
    cursor = conn.cursor()
    if no_template:
        cursor.execute('CREATE DATABASE ana_{};'.format(account))
    else:
        cursor.execute('CREATE DATABASE ana_{} '
                       'TEMPLATE ana_template;'.format(account))
    conn.close()


def deactivate(args, account):
    """Deactivate the node in anabroker

    :param argparse.namespace args: The parsed cli arguments
    :param int account: The account to deactivate

    """
    cursor = anabroker.cursor(args)
    LOGGER.debug('Deactivating account %i in anabroker', account)
    cursor.execute(TOGGLE_ACCOUNT_ACTIVE, {'a_id': account, 'active': False})
    cursor.close()
    redcache.clear_assignments(account)


def lookup(args, account):
    """Return the server connection information for the specified account.

    :param argparse.namespace args: The parsed cli arguments
    :param int account: The account # to lookup the server info for
    :return: dict
    :raises: NoAnalyticsDatabase

    """
    cursor = anabroker.cursor(args)
    cursor.execute(LOOKUP_ASSIGNMENT, {'a_id': account})
    if not cursor.rowcount:
        raise exceptions.NoAnalyticsDatabase
    data = dict(cursor.fetchone())
    cursor.close()
    return data


def unassign(args, account):
    """Remove the account from the analytics broker.

    :param argparse.namespace args: The parsed cli arguments
    :param int account: The account ID to remove

    """
    cursor = anabroker.cursor(args)
    LOGGER.debug('Removing assignment for %s from the analytics broker',
                 account)
    cursor.execute(REMOVE_ASSIGNMENT, {'a_id': account})
    cursor.close()
    redcache.clear_assignments(account)
