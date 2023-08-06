"""
Class Patterns that can be used to quickly write applications for working
with analytics databases.

"""
import logging
import multiprocessing
import os
from os import path
import queue
import signal
import sys
import threading
import time

from anadb_tools import anabroker, common


LOGGER = logging.getLogger(__name__)


class ThreadedIterator:

    DESCRIPTION = 'Iterate over values and perform work'
    MODULE = threading
    CHILD_CLASS = threading.Thread
    _TYPE = 'thread'
    _DEFAULT_CONCURRENCY = 4

    def __init__(self):
        self.arg_parser = self._create_cli_parser()
        self.args = common.parse_arguments(self.arg_parser)
        self.stop_event = self.MODULE.Event()
        self.work_dir = path.abspath(self.args.work_dir)
        if not path.exists(self.work_dir):
            LOGGER.error('Specified work directory does not exist: %s',
                         self.work_dir)
            sys.exit(1)
        self.error_file = path.join(
            self.work_dir, '{}.errors'.format(sys.argv[0].replace('.py', '')))
        self.progress_file = path.join(
            self.work_dir,
            '{}.progress'.format(sys.argv[0].replace('.py', '')))
        self.progress_lock = self.MODULE.Lock()
        self.work_queue = queue.Queue()

    def add_cli_arguments(self, parser):
        """Extend this method to add additional CLI arguments to the app.

        :param argparse.ArgumentParser parser: The parser to add args to

        """
        pass

    def on_start(self):
        """Extend this method to do work on start of each child/thread"""
        pass

    def process(self, value):
        """Extend this method to do the per-value processing."""
        raise NotImplementedError

    def validate_args(self):
        """Extend this method to evaluate CLI arguments on startup. Return
        `True` to process.

        :rtype: bool

        """
        return True

    def values(self):
        """Return a list of values to iterate over

        :rtype: list

        """
        raise NotImplementedError

    def run(self):
        """Main class entry point. Example Use:

        .. code::

            ThreadedAccountIterator().run()

        """
        if self.validate_args():
            try:
                self._execute()
            except KeyboardInterrupt:
                LOGGER.info('CTRL-C caught, shutting down')
                self.stop_event.set()
        else:
            LOGGER.info('Args did not validate, bailing out')

    def _create_cli_parser(self):
        """Creates an argument parser and returns the handle. Invokes
        `self.add_cli_arguments` to add additional CLI args easily.

        :return: argparse.ArgumentParser

        """
        parser = common.argument_parser(self.DESCRIPTION)
        parser.add_argument(
            '-j', '--concurrency', action='store',
            default=self._DEFAULT_CONCURRENCY, type=int,
            help='Concurrent {}s to use. Default: {}'.format(
                self._TYPE, self._DEFAULT_CONCURRENCY))
        parser.add_argument(
            '-w', '--work-dir', default=os.getcwd(),  action='store',
            help='Work file directory. Default: {}'.format(os.getcwd()))
        self.add_cli_arguments(parser)
        return parser

    def _execute(self):
        """Main logic for the application. You should not need to do anything
        here.

        """
        signal.signal(signal.SIGTERM, self._on_sigterm)
        processed = self._get_previously_processed()
        values = self.values()

        if processed:
            LOGGER.info('Skipping %i previously processed items',
                        len(processed))
            values = [v for v in values if v not in processed]

        summary = ('Processing {:,} values with a concurrency of {:,} '
                   'threads'.format(len(values), self.args.concurrency))
        LOGGER.info(summary)

        LOGGER.debug('Putting first 1k items in shared queue')
        for value in values[:1000]:
            self.work_queue.put(value)

        # Create and start the worker threads
        LOGGER.debug('Starting children')
        children = []
        for _index in range(0, self.args.concurrency):
            children.append(self.CHILD_CLASS(target=self._runner, daemon=False))
            children[-1].start()

        LOGGER.debug('Putting remaining items in shared queue')
        for value in values[1000:]:
            self.work_queue.put(value)

        # Wait until all the threads are finished. The ``signal.pause()``
        # technique is used to allow for catching the KeyboardInterrupt at the
        # top level.
        signal.signal(signal.SIGALRM, self._on_alarm)
        signal.alarm(5)
        while not self.stop_event.is_set() and not self.work_queue.empty():
            try:
                signal.pause()
            except KeyboardInterrupt:
                LOGGER.info('CTRL-C caught, signaling children to stop')
                self.stop_event.set()
                children[0].join()
            else:
                signal.alarm(5)

        while any([c.is_alive() for c in children]):
            LOGGER.debug('Waiting for children to exit')
            time.sleep(1)

        remaining = self.work_queue.qsize()
        count = len(values) - len(processed) - remaining
        LOGGER.info('Processed {:,} values {:,} remain'.format(
            count, remaining))

    def _get_previously_processed(self):
        """Return the set of previously processed items.

        :rtype: set

        """
        processed = set([])
        if path.exists(self.progress_file):
            with open(self.progress_file, 'r') as handle:
                for line in handle:
                    processed.add(int(line.strip()))
        return processed

    @staticmethod
    def _on_alarm(signum, _frame):
        """Invoked when the alarm is raised every 5 seconds while processing"""
        pass

    def _on_sigterm(self, _signum, _frame):
        """Set the stop event"""
        self.stop_event.set()

    def _runner(self):
        """Thread runner method. This method is invoked per thread and
        processes values until no more values are available for processing

        """
        self.on_start()

        # Loop while the stop event is not set & there are databases to process
        while not self.stop_event.is_set() and not self.work_queue.empty():

            # Exit if the stop event is set
            if self.stop_event.is_set():
                LOGGER.debug('Stop request received, exiting')
                break

            try:
                value = self.work_queue.get(True, 5)
            except queue.Empty:
                LOGGER.info('Queue is empty, exiting')
                self.stop_event.set()
                break

            try:
                result = self.process(value)
            except KeyboardInterrupt:
                self.stop_event.is_set()
                LOGGER.debug('Caught CTRL-C')
                continue

            # Write out the result to the appropriate log file
            log_file = self.progress_file if result else self.error_file
            self.progress_lock.acquire()
            with open(log_file, 'a') as handle:
                handle.write('{}\n'.format(value))
            self.progress_lock.release()

        LOGGER.debug('Exiting runner')


class MultiProcessIterator(ThreadedIterator):

    DESCRIPTION = 'Iterate over values and perform work in multiple processes'
    MODULE = multiprocessing
    CHILD_CLASS = multiprocessing.Process
    _DEFAULT_CONCURRENCY = multiprocessing.cpu_count()
    _TYPE = 'process'

    def __init__(self):
        super(MultiProcessIterator, self).__init__()
        self.work_queue = multiprocessing.Queue()


class ThreadedAccountIterator:

    DESCRIPTION = 'Iterate over all accounts and perform work'

    def __init__(self):
        self.arg_parser = self._create_cli_parser()
        self.args = common.parse_arguments(self.arg_parser)
        self.stop_event = threading.Event()
        self.work_dir = path.abspath(self.args.work_dir)
        if not path.exists(self.work_dir):
            LOGGER.error('Specified work directory does not exist: %s',
                         self.work_dir)
            sys.exit(1)
        self.error_file = path.join(
            self.work_dir, '{}.errors'.format(sys.argv[0].replace('.py', '')))
        self.progress_file = path.join(
            self.work_dir,
            '{}.progress'.format(sys.argv[0].replace('.py', '')))
        self.progress_lock = threading.Lock()
        self.work_queue = queue.Queue()

    def add_cli_arguments(self, parser):
        """Extend this method to add additional CLI arguments to the app.

        :param argparse.ArgumentParser parser: The parser to add args to

        """
        pass

    def process(self, account_id):
        """Extend this method to do the per-account processing."""
        raise NotImplementedError

    def run(self):
        """Main class entry point. Example Use:

        .. code::

            ThreadedAccountIterator().run()

        """
        try:
            self._execute()
        except KeyboardInterrupt:
            LOGGER.info('CTRL-C caught, shutting down')
            self.stop_event.set()

    def _create_cli_parser(self):
        """Creates an argument parser and returns the handle. Invokes
        `self.add_cli_arguments` to add additional CLI args easily.

        :return: argparse.ArgumentParser

        """
        parser = common.argument_parser(self.DESCRIPTION)
        parser.add_argument(
            '-t', '--threads', action='store', default=10, type=int,
            help='Quantity of threads for execution. Default: 10')
        parser.add_argument(
            '-w', '--work-dir', default=os.getcwd(),  action='store',
            help='Work file directory. Default: {}'.format(os.getcwd()))
        self.add_cli_arguments(parser)
        return parser

    def _execute(self):
        """Main logic for the application. You should not need to do anything
        here.

        """
        # Load in already processed databases
        processed = set([])
        if path.exists(self.progress_file):
            with open(self.progress_file, 'r') as handle:
                for line in handle:
                    processed.add(int(line.strip()))

        LOGGER.info('Fetching account database list')
        databases = anabroker.databases(self.args)

        # Add the databases to the queue, skipping over already deployed databases
        for index, database in enumerate(databases):
            if database['a_id'] in processed:
                LOGGER.debug('Skipped database for %s: already processed',
                             database['a_id'])
                continue
            self.work_queue.put(database['a_id'])

        summary = ('Checking to {:,} account databases with {:,} '
                   'threads'.format(len(databases) - len(processed),
                                    self.args.threads))
        LOGGER.info(summary)

        # Create and start the worker threads
        threads = []
        for _index in range(0, self.args.threads):
            thread = threading.Thread(target=self._thread_runner)
            thread.start()
            threads.append(thread)

        # Wait until all the threads are finished. The ``signal.pause()``
        # technique is used to allow for catching the KeyboardInterrupt at the
        # top level.
        signal.signal(signal.SIGALRM, self._on_alarm)
        signal.alarm(5)
        while not self.stop_event.is_set() and not self.work_queue.empty():
            try:
                signal.pause()
            except KeyboardInterrupt:
                LOGGER.info('CTRL-C caught, signaling threads to stop')
                self.stop_event.set()
                threads[0].join()
            else:
                signal.alarm(5)

        while any([t.is_alive() for t in threads]):
            LOGGER.debug('Waiting for threads to exit')
            time.sleep(1)

        checked = len(databases) - self.work_queue.qsize()
        summary = 'Checked {:,} databases, {:,} remain'.format(
            checked, self.work_queue.qsize())
        if processed:
            summary = (
                'Processed {:,} databases, {:,} in previous runs - '
                '{:,} remain'.format(
                    checked, len(processed),
                    self.work_queue.qsize()))
        LOGGER.info(summary)

    @staticmethod
    def _on_alarm(signum, _frame):
        """Invoked when the alarm is raised every 5 seconds while processing"""
        pass

    def _thread_runner(self):
        """Thread runner method. This method is invoked per thread and attempts
        to fetch databases from the queue until there are no more databases to
        fetch.

        One of two files are written to as a database is processed. If the
        deployment is success, the progress file is written to, otherwise
        error file is written to. The error log can be used to try and process
        again using the ``--account-file`` command-line switch.

        """
        # Loop while the stop event is not set & there are databases to process
        while not self.stop_event.is_set() and not self.work_queue.empty():

            # Exit if the stop event is set
            if self.stop_event.is_set():
                LOGGER.debug('Stop request received, exiting')
                break

            try:
                account_id = self.work_queue.get(True, 5)
            except queue.Empty:
                LOGGER.info('Queue is empty, exiting')
                self.stop_event.set()
                break

            # Process the account
            if self.process(account_id):
                log_file = self.progress_file
            else:
                log_file = self.error_file

            # Write out the result to the appropriate log file
            self.progress_lock.acquire()
            with open(log_file, 'a') as handle:
                handle.write('{}\n'.format(account_id))
            self.progress_lock.release()

        LOGGER.debug('Exiting thread runner')