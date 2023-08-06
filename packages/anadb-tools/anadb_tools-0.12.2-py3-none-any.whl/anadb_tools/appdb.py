"""
Common Method for interfacing with AppDB

"""
import datetime
import os

from anadb_tools import common, database

NOTE_TYPES = [
    'admin',
    'blog',
    'customers',
    'email',
    'fax',
    'imsg',
    'internal',
    'notification',
    'phone',
    'phoneautomation',
    'postal',
    'twitter',
    'zendesk',
    'website'
]

_SERVERS = {
    'prod': {
        'host': 'app.service.production.consul',
        'port': 6000,
        'dbname': 'app'
    },
    'staging': {
        'host': 'app.service.staging.consul',
        'port': 6000,
        'dbname': 'app'
    },
    'test': {
        'host': 'app.service.testing.consul',
        'port': 6000,
        'dbname': 'app'
    },
    'local': {
        'host': os.environ.get('APPDB_HOST', 'localhost'),
        'port': int(os.environ.get('APPDB_PORT', 5432)),
        'dbname': os.environ.get('APPDB_DBNAME', 'app')
    }
}

_INSERT_NOTE = """\
INSERT INTO notes (time, type, admin_user, subject, body, zendesk_ticket_id)
     VALUES (CURRENT_TIMESTAMP, %(type)s, %(admin_user)s, %(subject)s, 
             %(body)s, %(zendesk_ticket_id)s) RETURNING note_id;"""

_INSERT_NOTE_MATCH = """\
INSERT INTO note_matches (note_id, match_type, match_id)
     VALUES (%(note_id)s, %(match_type)s, %(match_id)s);"""


def connect(args, autocommit=True):
    """Returns a psycopg2 :class:`~psycopg2.extensions.connection` for
    the specified arguments, in autocommit mode.

    :param argparse.namespace args: The parsed cli arguments
    :param bool autocommit: Enable/Disable autocommit
    :rtype: :class:`~psycopg2.extensions.connection`

    """
    return database.connect(
        os.environ.get('APPDB_HOST', _SERVERS[args.environment]['host']),
        int(os.environ.get('APPDB_PORT', _SERVERS[args.environment]['port'])),
        os.environ.get('APPDB_DBNAME', _SERVERS[args.environment]['dbname']),
        os.environ.get('APPDB_USER', args.username), args.role,
        args.password, 'AppDB Password: ', autocommit)


def add_note(args, account, subject, body,
             note_type='internal', admin_user=None, zendesk_ticket_id=None):
    """Creates an account note. If ``note_type`` is specified, it must be one
    of the values in ``NOTE_TYPES``

    :param argparse.namespace args: The parsed cli arguments
    :param int account: The account to add the note for
    :param str subject: The note subject
    :param str body: The note body
    :param str note_type: The type of note, defaults to ``internal``
    :param str admin_user: The username who the note is attributed to
    :param int zendesk_ticket_id: If related to a zendesk ticket, specify the
                                  ticket ID.
    :raises: ValueError

    """
    if not admin_user:
        admin_user = common.get_username()

    if note_type not in NOTE_TYPES:
        raise ValueError('Invalid Note Type: {}'.format(note_type))

    conn = connect(args)
    cursor = conn.cursor()

    # Create the note
    cursor.execute(_INSERT_NOTE, {'type': note_type,
                                  'admin_user': admin_user,
                                  'subject': subject,
                                  'body': body,
                                  'zendesk_ticket_id': zendesk_ticket_id})
    note = cursor.fetchone()

    # Add the association
    cursor.execute(_INSERT_NOTE_MATCH, {'note_id': note['note_id'],
                                        'match_type': 'customers',
                                        'match_id': account})
    conn.close()
