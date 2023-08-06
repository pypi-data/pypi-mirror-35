#!/usr/bin/env python
"""
anadb-activate
==============

Sets an inactive account analytics database to active

"""
from anadb_tools import anadb
from anadb_tools import common

LOGGER = common.get_logger()


def execute(args):
    """What executes when your application is run.

    :param argparse.namespace args: The parsed cli arguments

    """
    anadb.activate(args, args.account)
    LOGGER.info('Account %s set to active and cache was cleared',
                args.account)


def main():
    """Invoked when the application is executed."""
    parser = common.argument_parser(
        'Sets an inactive account analytics database to active')
    parser.add_argument('-a', '--account', action='store', type=int,
                        required=True, help='The account to activate')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Increase output verbosity')
    execute(common.parse_arguments(parser))


if __name__ == '__main__':
    main()

