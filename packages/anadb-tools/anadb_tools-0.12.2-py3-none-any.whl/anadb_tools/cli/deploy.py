"""
anadb-deploy
============

Deploy DDL to all analytics databases, including the template database.

"""
import os
from os import path
try:
    import queue
except ImportError:
    import Queue as queue
import signal
import subprocess
import threading
import time

from anadb_tools import anabroker, common

ERROR_LOG = 'anadb-deploy.errors'
PROGRESS_LOG = 'anadb-deploy.progress'
TEMPLATE_LOG = 'anadb-deploy.template'

LOGGER = common.get_logger()
STOP = threading.Event()


def deploy(database, args):
    """Deploy the DDL to the specified database. Returns ``True`` on success.

    :param dict database: The database to deploy to
    :param argparse.namespace args: The parsed cli arguments
    :rtype: bool

    """
    hostname = '{}.{}'.format(database['hostname'], args.domain)
    command = ['psql', '-h', hostname, '-p', str(database['port']),
               '-f', args.filename, '-d', database['dbname']]
    if args.username:
        command += ['-U', args.username]
    LOGGER.debug('%r', command)
    LOGGER.info('Deploying to %s on %s:%i', database['dbname'],
                hostname, database['port'])
    start_time = time.time()
    pipe = subprocess.Popen(command,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdout, stderr = pipe.communicate()
    for line in stdout.strip().splitlines(True):
        if line.strip():
            LOGGER.debug(line.strip())
    for line in stderr.strip().splitlines(True):
        if line.strip():
            LOGGER.error(line.strip())
    if pipe.returncode:
        LOGGER.error('Error processing %s: %s', database['dbname'], stderr)
        return False
    duration = time.time() - start_time
    LOGGER.info('Deployed to %s in %.2f seconds', database['dbname'], duration)
    return True


def deploy_templates(args):
    """Deploy the DDL to the ana_template databases. They have their own
    log file, ``TEMPLATE_LOG`` that is used to prevent subsequent deployments.

    :param argparse.namespace args: The parsed cli arguments

    """
    deployed = set()
    template_log = log_path(args, TEMPLATE_LOG)
    if path.exists(template_log):
        with open(template_log, 'r') as handle:
            for line in handle:
                deployed.add(line.strip())

    for server in get_template_servers(args):
        if server['hostname'] in deployed:
            LOGGER.debug('%s is already deployed, skipping',
                         server['hostname'])
            continue
        if deploy(server, args):
            with open(template_log, 'a') as handle:
                handle.write('{}\n'.format(server['hostname']))
            LOGGER.info('Deployed to %(dbname)s on %(hostname)s:%(port)s',
                        server)


def get_template_servers(args):
    """Get the analytics database servers to deploy the ana_template changes to

    :param argparse.namespace args: The parsed cli arguments
    :rtype: list

    """
    servers = [s for s in anabroker.servers(args)]
    for index, row in enumerate(servers):
        servers[index]['dbname'] = 'ana_template'
    return servers


def log_path(args, filename):
    """Return the absolute path for the specified log file.

    :param argparse.namespace args: The parsed cli arguments
    :param str filename: The name of the logfile

    """
    if args.work_dir.startswith('/'):
        return path.normpath(path.join(args.work_dir, filename))
    return path.abspath(path.join(os.getcwd(), args.work_dir, filename))


def thread_runner(args, work_queue, progress_lock):
    """Thread runner method. This method is invoked per thread and attempts
    to fetch databases from the queue until there are no more databases to
    fetch.

    One of wwo files are written to as a database is processed. If the
    deployment is success, PROGRESS_LOG is written to, otherwise ERROR_LOG is
    written to. The error log can be used to try and deploy again using the
    ``--account-file`` command-line switch.

    :param argparse.namespace args: The parsed cli arguments
    :param Queue.Queue work_queue: The queue of databases to process
    :param threading.Lock progress_lock: Lock to use when writing progress info

    """
    # Loop while the stop event is not set and there are databases to process
    while not STOP.is_set() and not work_queue.empty():

        # Exit if the stop event is set
        if STOP.is_set():
            LOGGER.debug('Stop request received, exiting')
            break

        try:
            database = work_queue.get()
        except queue.Empty:
            LOGGER.info('Queue is empty, exiting')
            break

        # Deploy the DDL
        if deploy(database, args):
            log_file = log_path(args, PROGRESS_LOG)
        else:
            log_file = log_path(args, ERROR_LOG)

        # Write out the result to the appropriate log file
        progress_lock.acquire()
        with open(log_file, 'a') as handle:
            handle.write('{}\n'.format(database['a_id']))
        progress_lock.release()


def execute(args):

    # Deploy to the template databases
    deploy_templates(args)

    # If limiting to a subset of accounts from a file, load that info in
    accounts = None
    if args.account_file:
        with open(args.account_file, 'r') as handle:
            accounts = list(set([int(line.strip()) for line in handle]))

    LOGGER.info('Fetching account database list')
    databases = anabroker.databases(args, accounts)

    # Load in already deployed databases
    deployed = set([])
    if path.exists(log_path(args, PROGRESS_LOG)):
        with open(log_path(args, PROGRESS_LOG), 'r') as handle:
            for line in handle:
                deployed.add(int(line.strip()))

    progress_lock = threading.Lock()
    work_queue = queue.Queue()

    # Add the databases to the queue, skipping over already deployed databases
    for index, database in enumerate(databases):
        if database['a_id'] in deployed:
            LOGGER.debug('Skipped database for %s: already deployed',
                         database['a_id'])
            continue
        work_queue.put(database)

    LOGGER.info('Deploying to %i account databases with %i threads',
                len(databases) - len(deployed), args.threads)

    # Create and start the worker threads
    threads = []
    for _index in range(0, args.threads):
        thread = threading.Thread(target=thread_runner,
                                  args=(args, work_queue, progress_lock))
        thread.start()
        threads.append(thread)

    # Wait until all the threads are finished. The ``signal.pause()`` technique
    # is used to allow for catching the KeyboardInterrupt at the top level.
    while not STOP.is_set() and not work_queue.empty():
        try:
            signal.pause()
        except KeyboardInterrupt:
            LOGGER.info('CTRL-C caught, signaling threads to stop')
            STOP.set()
            threads[0].join()

    LOGGER.info('Deployed to {:,} databases'.format(
        len(databases) - work_queue.qsize()))


def main():
    parser = common.argument_parser('Deploy DDL to all analytics databases')
    parser.add_argument('filename', help='The path for the file to deploy')
    parser.add_argument('-t', '--threads',
                        action='store',
                        default=10,
                        type=int,
                        help='Quantity of threads for execution. Default: 10')
    parser.add_argument('-a', '--account-file',
                        action='store',
                        help='Only deploy to accounts listed in the specified '
                        'file')
    parser.add_argument('-w', '--work-dir',
                        action='store',
                        help='Work file directory. '
                        'Default: {}'.format(os.getcwd()),
                        default=os.getcwd())
    args = common.parse_arguments(parser)

    work_dir = log_path(args, '')
    if not path.exists(work_dir):
        common.exit_application('Work directory {} does not '
                                'exist.'.format(work_dir), 3)

    # Deploy all the things!
    try:
        execute(args)
    except KeyboardInterrupt:
        LOGGER.info('CTRL-C caught, shutting down')
        STOP.set()


if __name__ == '__main__':
    main()
