"""
Adds records to the v2.utilization_history record for each account on each
server.

"""
import io
import os
import threading

import psycopg2

from anadb_tools import anabroker, common, database, patterns

LOGGER = common.get_logger()

SERVER_LIST_SQL = """\
SELECT hostname, port FROM v2.servers WHERE offline is FALSE;"""

DATSIZE_SQL = """\
SELECT substring(datname FROM 5)::INT AS account_id,
       pg_database_size(datname) AS size_on_disk
  FROM pg_database
 WHERE datname LIKE $$ana_%$$
   AND datname NOT IN ('ana_default', 'ana_template');"""


MEASUREMENT_SQL = """\
INSERT INTO v2.utilization_history (account_id, hostname, size_on_disk)
     VAlUES (%(account_id)s, %(hostname)s, %(size_on_disk)s);"""

ROW_FORMAT = '{}\t{}\t{}\n'

class GatherUtilization(patterns.ThreadedIterator):

    DESCRIPTION = 'Gathers size on disk by server and account'

    def __init__(self):
        super(GatherUtilization, self).__init__()
        self.lock = threading.Lock()

    def process(self, server):
        LOGGER.info('Processing %s', server['hostname'])
        conn = database.connect(
            server['hostname'], server['port'], 'postgres',
            os.environ.get('ANADB_USER', self.args.username),
            self.args.role, self.args.password,
            'Analytics Database Password: ', True)
        cursor = conn.cursor()
        cursor.execute(DATSIZE_SQL)
        LOGGER.info('Returned size for %i databases', cursor.rowcount)

        buffer = io.StringIO()

        for row in cursor.fetchall():
            if row['account_id'] and row['size_on_disk']:
                buffer.write(ROW_FORMAT.format(
                    row['account_id'], server['hostname'],
                    row['size_on_disk']))
        buffer.seek(0)

        self.lock.acquire(True)
        LOGGER.info('Writing records for %s', server['hostname'])
        cursor = anabroker.connect(self.args).cursor()
        try:
            cursor.copy_from(buffer, 'v2.utilization_history',
                             columns=('account_id', 'hostname', 'size_on_disk'))
        except psycopg2.Error as error:
            LOGGER.error('Failed to write utilization history for %s: %s',
                         server['hostname'], error)
        self.lock.release()

    def values(self):
        cursor = anabroker.connect(self.args).cursor()
        cursor.execute(SERVER_LIST_SQL)
        return [dict(row) for row in cursor.fetchall()]


def main():
    GatherUtilization().run()


if __name__ == '__main__':
    main()
