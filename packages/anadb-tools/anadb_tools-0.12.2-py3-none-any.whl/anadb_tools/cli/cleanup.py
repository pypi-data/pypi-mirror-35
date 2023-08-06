"""
anadb-cleanup
=============

Backup and Delete analytics databases for closed accounts.

"""
from anadb_tools import anabroker
from anadb_tools import anadb
from anadb_tools import appdb
from anadb_tools import common
from anadb_tools import database
from anadb_tools import redcache

LOGGER = common.get_logger()

GET_CLOSED_ACCOUNTS = """\
SELECT a.a_id, a.status_id, max(ap.date_closed) as date_closed
  FROM accounts AS a
  JOIN account_packages AS ap ON ap.a_id = a.a_id
 WHERE a.status_id = 7
 GROUP BY a.a_id, a.status_id
HAVING max(ap.date_closed) <= current_timestamp - interval %(lower_bound)s
   AND max(ap.date_closed) >= current_timestamp - interval %(upper_bound)s
 ORDER BY a.a_id ASC;"""

IS_ACCOUNT_ACTIVE = """\
SELECT a_id, hostname, port, dbname, active, external_rollups
  FROM ana_db_locations WHERE a_id = %(a_id)s;"""


def execute(args):
    """Backup and remove all customer databases that were closed between X and
    Y days ago, where X and Y are specified in the CLI arguments as the upper
    and lower bound values.

    :param argparse.namespace args: The CLI arguments

    """
    accounts = get_closed_accounts(args)
    LOGGER.info('Fetching anadb assignment information for %i accounts',
                len(accounts))

    assignments = anabroker.databases(args, accounts)
    LOGGER.info('Processing %i closed accounts with analytics databases',
                len(assignments))

    for assignment in assignments:
        LOGGER.info('Processing account %s on %s:%s', assignment['a_id'],
                    assignment['hostname'], assignment['port'])
        anadb.deactivate(args, assignment['a_id'])
        backup_path = database.backup(args, assignment['hostname'],
                                      assignment['port'], assignment['dbname'])
        appdb.add_note(args, assignment['a_id'], 'Analytics Backup',
                       'Customer analytics database backed up to {}'.format(
                           backup_path))
        database.drop(args, assignment['hostname'], assignment['port'],
                      assignment['dbname'])
        anadb.unassign(args, assignment['a_id'])
        appdb.add_note(args, assignment['a_id'], 'Analytics Cleanup',
                       'Customer analytics database removed')
        redcache.clear_assignments(assignment['a_id'])

    anabroker.close()
    LOGGER.info('Backed up and removed analytics databases for %i '
                'closed accounts',
                len(assignments))


def get_closed_accounts(args):
    """Return a list of closed accounts meeting the upper and lower bounds
    criteria from the CLI arguments.

    :param argparse.namespace args: The CLI arguments
    :rtype: list

    """
    LOGGER.info('Fetching all closed accounts between %s and %s',
                common.get_date(args.upper_bound),
                common.get_date(args.lower_bound))
    conn = appdb.connect(args)
    cursor = conn.cursor()
    cursor.execute(GET_CLOSED_ACCOUNTS,
                   {'lower_bound': '{} days'.format(args.lower_bound),
                    'upper_bound': '{} days'.format(args.upper_bound)})
    accounts = set()
    for row in cursor:
        accounts.add(row['a_id'])
    conn.close()
    return list(accounts)


def main():
    parser = common.argument_parser('Backup and Delete analytics databases'
                                    ' for closed accounts')
    database.add_backup_arguments(parser)
    parser.add_argument('-l', '--lower-bound', type=int, action='store',
                        help='The minimum number of days for an account to be '
                             'closed for it to be processed. Default: 90',
                        default=90)
    parser.add_argument('-u', '--upper-bound', type=int, action='store',
                        help='The maximum number of days for an account to be '
                             'closed for it to be processed. Default: 120',
                        default=120)
    args = common.parse_arguments(parser)
    execute(args)


if __name__ == '__main__':
    main()
