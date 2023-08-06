"""
anadb-s3backup
==============

Backup an analytics database to Amazon S3

"""
from anadb_tools import anadb
from anadb_tools import appdb
from anadb_tools import database
from anadb_tools import common


def execute(args):
    """Backup a customer's analytics database to Amazon S3

    :param argparse.namespace args: The parsed cli arguments

    """
    # Figure out where we are moving the account from
    location = anadb.lookup(args, args.account)

    # Backup the database to S3
    backup_path = database.backup(args,
                                  location['hostname'],
                                  location['port'],
                                  location['dbname'])

    # Add the database note specifying where the backup was made to
    appdb.add_note(args, args.account, 'Analytics Backup',
                   'Customer analytics database backed up to {}'.format(
                       backup_path))


def main():
    """Invoked when the application is executed."""
    parser = common.argument_parser('Backup a customers analytics database to'
                                    'Amazon S3')
    parser.add_argument('-a', '--account', help='Account to backup', type=int,
                        action='store', required=True)
    database.add_backup_arguments(parser)
    execute(common.parse_arguments(parser))


if __name__ == '__main__':
    main()
