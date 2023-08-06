"""
anadb-orphans
=============

Removes Orphaned analytics databases

"""
import arrow

from anadb_tools import anabroker, appdb, common, database

LOGGER = common.get_logger()

S3_PATH = 'backup/anadb-orphans/%(date)s/%(hostname)s/%(filename)s'


DB_LIST = """\
SELECT substring(datname, 5)::int AS account, datname AS dbname
  FROM pg_database
 WHERE datname <> 'ana_template'
   AND datname LIKE 'ana_%';
"""

NODE_ASSIGNMENT = """\
SELECT hostname
  FROM ana_db_locations
 WHERE a_id = %(a_id)s;
"""

ACCOUNT_STATUS = "SELECT status_id FROM accounts WHERE a_id = %(a_id)s;"


def get_date(negative_offset):
    """Return a formatted date from the current day - the specified negative
    offset in days.

    :param int negative_offset: Number of days to subtract from today
    :rtype: str

    """
    utc = arrow.utcnow()
    return utc.replace(days=-negative_offset).format('YYYY-MM-DD')


def get_orphans(args):
    """Return a list of orphaned databases.

    :param argparse.namespace args: The CLI arguments
    :return: list

    """
    LOGGER.info('Checking %s for orphans', args.host)
    conn = database.connect(args.host, args.port, 'postgres', args.username,
                            args.password)
    cursor = conn.cursor()
    anabroker_conn = anabroker.connect(args)
    anabroker_cursor = anabroker_conn.cursor()
    appdb_conn = appdb.connect(args)
    appdb_cursor = appdb_conn.cursor()

    databases = []

    cursor.execute(DB_LIST)
    LOGGER.debug('Examining %i databases', cursor.rowcount)
    for row in cursor:
        anabroker_cursor.execute(NODE_ASSIGNMENT, {'a_id': row['account']})
        if not anabroker_cursor.rowcount:
            LOGGER.debug('Account %i is not found', row['account'])
            appdb_cursor.execute(ACCOUNT_STATUS, {'a_id': row['account']})
            if appdb_cursor.rowcount:
                account = appdb_cursor.fetchone()
                if account['status_id'] != 7:
                    LOGGER.error('Account %i in status %i is not in anabroker',
                                 row['account'], account['status_id'])
                    raise ValueError('Missing AnaBroker Record!')
            databases.append(row['dbname'])
        else:
            assignment = anabroker_cursor.fetchone()
            if assignment['hostname'] != args.host:
                LOGGER.debug('Account %i is assigned to %s, not %s',
                             row['account'], assignment['hostname'], args.host)
                databases.append(row['dbname'])
            else:
                LOGGER.debug('Account %i is ok', row['account'])
    anabroker_conn.close()
    conn.close()
    return databases


def execute(args):
    """Backup and remove all customer databases that were closed between X and
    Y days ago, where X and Y are specified in the CLI arguments as the upper
    and lower bound values.

    :param argparse.namespace args: The CLI arguments

    """
    orphans = get_orphans(args)
    if not orphans:
        LOGGER.info('AWesome, no orphans found')
        return

    LOGGER.info('Processing %i orphans', len(orphans))
    for orphan in orphans:
        database.backup(args, args.host, args.port, orphan)
        database.drop(args, args.host, args.port, orphan)

    LOGGER.info('Backed up and removed %i orphaned analytics databases',
                len(orphans))


def main():
    parser = common.argument_parser('Backup and remove orphaned databases')
    database.add_backup_arguments(parser)
    group = common.connection_arguments(parser)
    group.add_argument('-h', '--host', type=str, action='store',
                       help='The analytics database server to process',
                       required=True)
    group.add_argument('-p', '--port', type=int, action='store',
                       help='The analytics database server port',
                       default=5432)
    execute(common.parse_arguments(parser))


if __name__ == '__main__':
    main()
