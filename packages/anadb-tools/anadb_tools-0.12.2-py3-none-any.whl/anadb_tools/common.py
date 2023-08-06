"""
Common methods that are shared by the various utilities

"""
import argparse
import arrow
import logging
import os
from os import path
import pwd
import sys

from anadb_tools import __version__

LOGGER = logging.getLogger(__name__)

LOGGING_FORMAT = ('[%(asctime)-15s] %(levelname)-8s %(processName)-10s '
                  '%(threadName)-10s %(name)-25s %(message)s')

_connection_args_added = False


def argument_parser(description):
    """Return the base argument parser for CLI applications.

    :param str description: The application description
    :return: :class:`~argparse.ArgumentParser`

    """
    return argparse.ArgumentParser(description, conflict_handler='resolve')


def configure_logging(args):
    """Configure Python logging.

    :param argparse.namespace args: The parsed cli arguments

    """
    level = logging.WARNING
    if args.verbose:
        level = logging.INFO
    elif args.debug:
        level = logging.DEBUG
    filename = args.log_file if args.log_file else None
    if filename:
        filename = path.abspath(filename)
        if not path.exists(path.dirname(filename)):
            filename = None
    logging.basicConfig(level=level, filename=filename,
                        format=LOGGING_FORMAT)

    # Set a default level for botocore that wont conflict with debug
    logger = logging.getLogger('botocore')
    logger.setLevel(logging.INFO)

    # urilib3 is chatty, even on INFO
    _silence_urllib3()


def connection_arguments(parser):
    """Add the connection arguments group, returning the handle to add
    additional connection CLI arguments. If this method is not invoked,
    the default connection arguments will automatically be added.

    :param argparse.ArgumentParser parser: The argument parser
    :rtype: argparse._ArgumentGroup

    """
    global _connection_args_added
    _connection_args_added = True
    group = parser.add_argument_group(title='Connection options')
    group.add_argument('-e', dest='environment', action='store',
                       choices=['prod', 'staging', 'test', 'local'],
                       help='The environment to execute in. Default: prod',
                       default='prod')
    group.add_argument('-U', '--username', action='store',
                       default=get_username(),
                       help='The PostgreSQL username to operate as. '
                            'Default: {}'.format(get_username()))
    group.add_argument('-W', '--password', action='store_true',
                       help='Force password prompt (should happen '
                            'automatically)')
    group.add_argument('--role', action='store',
                       help='Role to assume when connecting to a database')
    return group


def exit_application(message=None, code=0):
    """Exit the application displaying the message to either stdout or stderr
    based upon the exist code.

    :param str message: The exit message
    :param int code: The exit code (default: 0)

    """
    if not code:
        if message:
            get_logger().info(message.strip())
        sys.exit(0)
    if message:
        get_logger().error(message.strip())
    sys.exit(code)


def get_application():
    """Return the name of the current application

    :rtype: str

    """
    name = sys.argv[0].split(os.sep)[-1]
    return name[:-3] if name.endswith('.py') else name


def get_date(negative_offset):
    """Return a formatted date from the current day - the specified negative
    offset in days.

    :param int negative_offset: Number of days to subtract from today
    :rtype: str

    """
    utc = arrow.utcnow()
    return utc.replace(days=-negative_offset).format('YYYY-MM-DD')


def get_logger():
    """Return a logger for the current application.

    :rtype: logging.Logger

    """
    return logging.getLogger(get_application())


def get_username():
    """Return the username of the current process.

    :rtype: str

    """
    return pwd.getpwuid(os.getuid())[0]


def parse_arguments(parser):
    """Parse the arguments and perform common tasks for the parsed arguments.

    :param argparse.ArgumentParser parser: The argument parser
    :return argparse.namespace: The parsed cli arguments

    """
    _append_common_arguments(parser)

    args = parser.parse_args()

    # Print version and exit if specified
    if args.version:
        print('{} (anadb-tools {})'.format(get_application(), __version__))
        sys.exit(0)

    configure_logging(args)
    get_logger().info('Application started using anadb-tools v%s in %s',
                      __version__, args.environment)
    return args


def _append_common_arguments(parser):
    """Appends common argument parser options to the
    :class:`~argparse.ArgumentParser`.

    :param argparse.ArgumentParser parser: The argument parser

    """
    if not _connection_args_added:
        connection_arguments(parser)

    group = parser.add_argument_group(title='Logging options')
    group.add_argument('-L', '--log-file', action='store',
                       help='Log to the specified filename. If not specified, '
                            'log output is sent to STDOUT')
    group.add_argument('-v', '--verbose', action='store_true',
                       help='Increase output verbosity')
    group.add_argument('--debug', action='store_true',
                       help='Extra verbose debug logging')
    parser.add_argument('-V', '--version', action='store_true',
                        help='output version information, then exit')


def _silence_urllib3():
    """vendored urilib3 can be chatty, hide its debug output in our logging"""
    for name in ['botocore.vendored.requests.packages.urllib3.connectionpool',
                 'requests.packages.urllib3.connectionpool']:
        logger = logging.getLogger(name)
        logger.setLevel(logging.WARNING)
