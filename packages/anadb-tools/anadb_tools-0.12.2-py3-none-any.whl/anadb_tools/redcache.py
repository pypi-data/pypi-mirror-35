"""
Functionality for clearing analytics related data cached in redcache

"""
import json
import logging
import os
import socket

import consulate
import redis


LOGGER = logging.getLogger(__name__)

CACHE_KEYS = [
    'analytics_db_host_{}',
    'aweber_app_analytics_db_host_{}',
    'analytics_broker.assignment.{}',
    'ana_db_locations:{}'
]


def clear_assignments(account):
    """Clear anabroker assignments in memcached and redis.

    :param account:

    """
    _clear_memcached(account)
    _clear_redis(account)


def _clear_memcache(server, account):
    """Clear the memcached keys for the specified account on the cache host.

    :param (str, int) server: The server to clear cache on
    :param int account: The account to clear

    """
    LOGGER.debug('Clearing cache for %i on %r', account, server)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    try:
        sock.connect(server)
    except socket.timeout:
        LOGGER.warning('Failed to clear cache for %i on %r', account, server)
        return
    for key in CACHE_KEYS:
        try:
            sock.sendall(
                'delete {}\r\n'.format(key.format(account)).encode('LATIN-1'))
            LOGGER.debug('memcached response: %s', sock.recv(1024).strip())
        except socket.timeout:
            LOGGER.warning('Failed to clear cache for %i on %r', account,
                           server)
            pass
    sock.close()


def _clear_memcached(account):
    """Clear memcached for the specified account.

    :param int account: The account to clear

    """
    for server in _get_memcached_hosts():
        _clear_memcache(server, account)


def _clear_redis(account):
    """Clear redis for the specified account.

    :param int account: The account to clear

    """
    for server in _get_redis_hosts():
        client = redis.StrictRedis(host=server[0], port=server[1], db=0)
        result = client.delete(*[k.format(account) for k in CACHE_KEYS])
        LOGGER.debug('%r clear result: %r', server, result)


def _consul_client():
    """Return a Consul client.

    :rtype: consulate.Consul

    """
    return consulate.Consul(
        host=os.environ.get('CONSUL_HOST', 'consul.service.production.consul'),
        port=int(os.environ.get('CONSUL_PORT', '80')))


def _get_memcached_hosts():
    """Return the list of memcached hosts.

    :return: list

    """
    consul = _consul_client()
    value = consul.kv.get('redcache/memcache/servers')
    return [_host_tuple(s) for s in json.loads(value)]


def _get_redis_hosts():
    """Return the list of memcached hosts.

    :return: list

    """
    consul = _consul_client()
    value = consul.kv.get('redcache/redis/servers')
    return [_host_tuple(s) for s in json.loads(value)]


def _host_tuple(value):
    """Return a tuple from an addr:port string.

    :rtype: tuple(str, int)

    """
    parts = value.split(':')
    return parts[0], int(parts[1])
