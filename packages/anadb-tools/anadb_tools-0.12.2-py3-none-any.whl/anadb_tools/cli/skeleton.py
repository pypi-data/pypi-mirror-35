"""
Create a skeleton anadb_tools CLI application

"""
import argparse
import sys

SIMPLE = """\
#!/usr/bin/env python
\"\"\"
%(name)s
%(underline)s

Skeleton anadb-tools application

\"\"\"
from anadb_tools import anabroker
from anadb_tools import anadb
from anadb_tools import common
from anadb_tools import exceptions

LOGGER = common.get_logger()


def execute(args):
    \"\"\"What executes when your application is run.

    :param argparse.namespace args: The parsed cli arguments

    \"\"\"


def main():
    \"\"\"Invoked when the application is executed.\"\"\"
    parser = common.argument_parser('Application Description')
    execute(common.parse_arguments(parser))


if __name__ == '__main__':
    main()

"""

THREADED = """\
#!/usr/bin/env python
\"\"\"
%(name)s
%(underline)s

Skeleton threaded anadb-tools application. This template reads in a file line
by line, adding the line to a queue that is shared across threads. Worker
threads act on the queue. The app will pause every ``MAX_QUEUE_SIZE`` waiting
for the the queue to drain before resuming.

\"\"\"
import Queue
import sys
import threading
import time

from anadb_tools import anabroker
from anadb_tools import anadb
from anadb_tools import common
from anadb_tools import exceptions

LOGGER = common.get_logger()
MAX_QUEUE_SIZE=100000


class Worker(threading.Thread):
    \"\"\"Simple implementations of the WorkerThread should only need to
    implement the ``Worker.process`` method.

    \"\"\"

    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        super(Worker, self).__init__(group, target, name, args, kwargs)
        self.cliargs = kwargs['cliargs']
        self.queue = kwargs['queue']
        self.done = kwargs['done']
        self.error_exit = kwargs['error_exit']

    def run(self):
        \"\"\"This method iterates over the queue until the ``done`` event is
        set, or if it needs to exit due to an error condition.

        \"\"\"
        while not self.done.is_set() and not self.error_exit.is_set():
            try:
                self.process(self.queue.get(False))
            except exceptions.NoAnalyticsDatabase as error:
                # This is an example exception block for exiting when there is
                # an error
                LOGGER.error('Error connecting to database: %%r', error)
                if not self.error_exit.is_set():
                    self.error_exit.set()
                break
            except Queue.Empty:
                if self.done.is_set():
                    break
                time.sleep(1)
                continue
        LOGGER.debug('Exiting thread %%r', self)

  def process(self, value):
    \"\"\"Process the value]\"\"\"
    pass


def build_payload(args, line):
    \"\"\"This method can be used to transform the line input into something
    more specific for processing.

    :param argparse.namespace args: The parsed cli arguments
    :param str line: The line to build the payload from

    \"\"\"
    return line


def execute(args):
    \"\"\"What executes when your application is run. It will spawn the
    specified number of threads, reading in the data from the specified file,
    adding them to the shared queue. The worker threads will work the queue,
    and the application will exit when the queue is empty.

    :param argparse.namespace args: The parsed cli arguments

    \"\"\"
    queue = Queue.Queue()
    done = threading.Event()
    error_exit = threading.Event()
    workers = []

    LOGGER.debug('Creating %%i worker threads', args.threads)
    for index in range(0, args.threads):
        worker = Worker(kwargs={'queue': queue,
                                'done': done,
                                'error_exit': error_exit,
                                'cliargs': args})
        worker.start()
        workers.append(worker)

    LOGGER.debug('Processing the file')
    for line in args.file:

        # This can happen due to a CTRL-C or other exceptions
        if error_exit.is_set():
            break

        # The return value of ``build_payload`` is added to the queue
        queue.put(build_payload(args, line))

        # If the queue exceeds the maximum size, sleep until it's empty
        while queue.qsize() >= MAX_QUEUE_SIZE:
            LOGGER.debug('Waiting for space in queue')
            start_time = time.time()
            while not queue.empty():
                time.sleep(5)
            LOGGER.debug('Resumed after %%.2f seconds',
                         time.time() - start_time)

    # All of the data has been added to the queue, wait for things to finish
    LOGGER.debug('Waiting for queue to empty')
    while not queue.empty():
        if error_exit.is_set():
            break
        time.sleep(1)

    # Flag that we're done
    done.set()

    # Wait for all of the threads to stop
    LOGGER.debug('Waiting for threads to stop')
    while any([worker.is_alive() for worker in workers]):
        time.sleep(1)

    LOGGER.debug('Processing complete')


def main():
    \"\"\"Invoked when the application is executed.\"\"\"
    parser = common.argument_parser('Build out files to process')
    parser.add_argument('-f', '--file', type=argparse.FileType('r'),
                        default=sys.stdin,
                        help='The file to process. Default: stdin')
    parser.add_argument('-t', '--threads', default=10, type=int,
                        help='Worker threads. Default: 10')
    execute(common.parse_arguments(parser))


if __name__ == '__main__':
    main()
"""


def parse_cli_arguments():
    parser = argparse.ArgumentParser('Generate a skeleton CLI application')
    parser.add_argument('-t', '--type', choices=['simple', 'threaded'],
                        default='simple',
                        help='The type of skeleton app to generate. '
                             'Default: simple')
    parser.add_argument('-f', '--file', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Where to write the skeleton to. Default: stdout')
    parser.add_argument('name', type=str, action='store',
                        help='The name of the application')
    return parser.parse_args()


def main():
    args = parse_cli_arguments()

    if args.type == 'simple':
        template = SIMPLE
    elif args.type == 'threaded':
        template = THREADED
    else:
        raise ValueError

    values = {'name': args.name,
              'underline': ('{:=<%i}' % len(args.name)).format('')}

    args.file.write(template % values)
