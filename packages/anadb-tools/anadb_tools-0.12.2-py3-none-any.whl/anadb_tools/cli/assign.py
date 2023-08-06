"""
anadb-create
============

Iterate over the ``public.assignment_requests`` database, creating new
analytics databases

"""
import random

from anadb_tools import anabroker
from anadb_tools import anadb
from anadb_tools import common
from anadb_tools import database
from anadb_tools import exceptions

LOGGER = common.get_logger()


def pending_accounts(args):
    """Generator that returns records for accounts that has yet to have their
    databases created. The method queries one row at a time in an attempt to
    prevent race conditions.

    :param argparse.namespace args: The parsed cli arguments
    :rtype: list(dict)

    """
    cursor = anabroker.cursor(args)
    while True:
        cursor.execute('SELECT id AS a_id'
                       '  FROM assignment_requests'
                       ' WHERE processed IS FALSE'
                       ' ORDER BY created ASC LIMIT 1;')
        if not cursor.rowcount:
            cursor.close()
            break
        yield cursor.fetchone()


def populate_tables(args, account, server):
    """Populate the database with the initial content required for the
    analytics database to function properly.

    :param argparse.namespace args: The parsed cli arguments
    :param int account: The account to populate the initial tables for
    :param dict server: The server to populate the data on

    """
    LOGGER.info('Populating initial tables for %s', account)
    conn = database.connect(server['hostname'], server['port'],
                            'ana_{}'.format(account), args.username,
                            args.role, args.password)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ana.customers (id) VALUES (%(a_id)s);",
                   {'a_id': account})
    if not cursor.rowcount:
        LOGGER.error('Error inserting account: %s', account)
        raise exceptions.OperationError('Account Insertion Error')
    cursor.execute("INSERT INTO ana.event_types VALUES "
                   "  (1, 'Page Hit', %(a_id)s), (2, 'Sale', %(a_id)s),"
                   "  (3, 'CPC', %(a_id)s), (4, 'CPM', %(a_id)s);",
                   {'a_id': account})
    if not cursor.rowcount:
        LOGGER.error('Error event_types account: %s', account)
        raise exceptions.OperationError('Event Types Insertion Error')
    cursor.execute("INSERT INTO ana.url_profiles VALUES "
                   "  (1, 'awt_value', 'awt_note', 'Default', %(a_id)s);",
                   {'a_id': account})
    if not cursor.rowcount:
        LOGGER.error('Error inserting account: %s', account)
        raise exceptions.OperationError('Pageview URL Profile Insertion Error')
    conn.close()


def random_assignment(args):
    """Select a server at random from the currently active servers.

    :param argparse.namespace args: The parsed cli arguments

    """
    servers = anabroker.servers(args, active_only=True, assignable_only=True)
    if not servers:
        common.exit_application('No analytics servers allowing new databases')

    LOGGER.info('Processing pending assignments assigning against %i servers '
                'at random', len(servers))
    count = 0
    for row in pending_accounts(args):
        process_assignment(args, row['a_id'],
                           servers[random.randint(0, len(servers) - 1)])
        count += 1
    if not count:
        LOGGER.info('No pending accounts found')
    else:
        LOGGER.info('%i accounts have been processed', count)


def process_assignment(args, account, server):
    """Process the individual account asssignment to the specified server.

    :param args:
    :param account:
    :param server:
    :return:
    """
    LOGGER.info('Processing account %s', account)
    anadb.create(args, server['hostname'], server['port'], account)
    populate_tables(args, account, server)
    anadb.assign(args, account, server['hostname'])
    set_processed(args, account)
    LOGGER.info('Account %s database setup complete', account)


def set_processed(args, account):
    """Generator that returns records for accounts that has yet to have their
    databases created. The method queries one row at a time in an attempt to
    prevent race conditions.

    :rtype: list(dict)

    """
    cursor = anabroker.cursor(args)
    cursor.execute('UPDATE assignment_requests '
                   '   SET processed = TRUE '
                   ' WHERE id = %(account)s', {'account': account})
    cursor.close()


def execute(args):
    if args.method == 'random':
        random_assignment(args)
    else:
        common.exit_application('{} not implemented'.format(args.method), 1)


def main():
    parser = common.argument_parser('Create new analytics databases')
    parser.add_argument('-m', '--method',
                        action='store',
                        choices=['random', 'best_guess'],
                        default='random',
                        help='Method used to choose which server to place an '
                        'account database on. Default: random')
    execute(common.parse_arguments(parser))


if __name__ == '__main__':
    main()
