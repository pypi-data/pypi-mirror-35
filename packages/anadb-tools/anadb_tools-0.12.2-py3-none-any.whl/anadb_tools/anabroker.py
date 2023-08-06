"""
Common Method for interfacing with anabroker

"""
import logging
import os

from anadb_tools import database

LOGGER = logging.getLogger(__name__)

GET_DATABASES = """\
SELECT a_id, hostname, port, dbname, active, external_rollups
  FROM ana_db_locations
 ORDER BY a_id;"""

GET_FILTERED_DATABASES = """\
SELECT a_id, hostname, port, dbname, active, external_rollups
  FROM ana_db_locations
 WHERE a_id = ANY(%(accounts)s)
 ORDER BY a_id;"""

GET_SERVERS = """\
SELECT hostname, port, active, allow_new_db
  FROM db_nodes
 WHERE active IS TRUE
 ORDER BY hostname ;"""


_SERVERS = {
    'prod': {
        'host': 'anabroker.service.production.consul',
        'port': 5432,
        'dbname': 'analytics_broker'
    },
    'staging': {
        'host': 'anabroker.service.staging.consul',
        'port': 5432,
        'dbname': 'analytics_broker'
    },
    'test': {
        'host': 'appbroker.service.testing.consul',
        'port': 5432,
        'dbname': 'analytics_broker'
    },
    'local': {
        'host': os.environ.get('ANABROKER_HOST', 'localhost'),
        'port': int(os.environ.get('ANABROKER_PORT', 5432)),
        'dbname': os.environ.get('ANABROKER_DBNAME', 'postgres')
    }
}

_CONNECTION = None


def connect(args, autocommit=True):
    """Returns a psycopg2 :class:`~psycopg2.extensions.connection` for
    the specified arguments, in autocommit mode.

    :param argparse.namespace args: The parsed cli arguments
    :param bool autocommit: Enable/Disable autocommit
    :rtype: :class:`~psycopg2.extensions.connection`

    """
    global _CONNECTION
    if _CONNECTION and not _CONNECTION.closed:
        return _CONNECTION

    host = os.environ.get('ANABROKER_HOST', _SERVERS[args.environment]['host'])
    port = int(os.environ.get('ANABROKER_PORT',
                              _SERVERS[args.environment]['port']))
    dbname = os.environ.get('ANABROKER_DBNAME',
                            _SERVERS[args.environment]['dbname'])
    user = os.environ.get('ANABROKER_USER', args.username)
    _CONNECTION = database.connect(host, port, dbname, user, args.role,
                                   args.password,
                                   'Analytics Broker Password: ',
                                   autocommit)
    return _CONNECTION


def close():
    """Close the cached anabroker connection."""
    global _CONNECTION
    _CONNECTION.close()
    _CONNECTION = None


def cursor(args):
    """Use a module-wide connection to get a cursor in anabroker.

    :param argparse.namespace args: The parsed cli arguments

    """
    global _CONNECTION

    if not _CONNECTION:
        _CONNECTION = connect(args)
    return _CONNECTION.cursor()


def databases(args, accounts=None):
    """Return a list of all of the databases that are configured in AnaBroker.

    :param argparse.namespace args: The parsed cli arguments
    :param list accounts: An optional list of accounts to limit the result to
    :return: list

    """
    _cursor = cursor(args)
    if accounts:
        _cursor.execute(GET_FILTERED_DATABASES, {'accounts': accounts})
    else:
        _cursor.execute(GET_DATABASES)
    data = [row for row in _cursor]
    _cursor.close()
    return data


def servers(args, active_only=False, assignable_only=False):
    """Return a list of all of the active database servers in anabroker.

    :param argparse.namespace args: The parsed cli arguments
    :param bool active_only: Filter servers to only active ones
    :param bool assignable_only: Filter servers to only assignable
    :return: list

    """
    _cursor = cursor(args)
    _cursor.execute(GET_SERVERS)
    data = [dict(row) for row in _cursor]
    _cursor.close()
    if active_only:
        data = [row for row in data if row['active']]
    if assignable_only:
        data = [row for row in data if row['allow_new_db']]
    return data
