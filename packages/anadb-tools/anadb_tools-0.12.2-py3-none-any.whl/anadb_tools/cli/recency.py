"""
anadb-orphans
=============

Removes Orphaned analytics databases

"""
import datetime

from anadb_tools import anadb, common

LOGGER = common.get_logger()

SQL = """\
WITH delivery AS (SELECT max(event_time) FROM ana.sent_messages),
     open AS (SELECT max(event_time) FROM ana.opens),
     click AS (SELECT max(event_time) FROM ana.clicks)
     SELECT delivery.max AS most_recent_delivery,
            open.max AS most_recent_open,
            click.max AS most_recent_click
       FROM delivery, open, click;
"""


def execute(args):
    """Backup and remove all customer databases that were closed between X and
    Y days ago, where X and Y are specified in the CLI arguments as the upper
    and lower bound values.

    :param argparse.namespace args: The CLI arguments

    """
    rows = []
    for account in args.account:
        LOGGER.debug('Processing account %s', account)
        anadb_conn = anadb.connect(args, account)
        cursor = anadb_conn.cursor()
        cursor.execute(SQL)
        data = cursor.fetchone()
        rows.append('{: <10}   {}  {}  {}'.format(
            account,
            data['most_recent_delivery'].isoformat(),
            data['most_recent_open'].isoformat(),
            data['most_recent_click'].isoformat()))
        anadb_conn.close()
    print('Account      Last Delivery              Last Open                '
          '  Last Click')
    print('-----------------------------------------------------------------'
          '---------------------------')
    for row in rows:
        print(row)
    print('-----------------------------------------------------------------'
          '---------------------------')
    print('Report Time: {}'.format(datetime.datetime.now().isoformat()))


def main():
    parser = common.argument_parser('Get the recency of metrics by account')
    parser.add_argument('account', help='The account ID for recency metrics',
                        type=int, nargs='+')
    execute(common.parse_arguments(parser))


if __name__ == '__main__':
    main()
