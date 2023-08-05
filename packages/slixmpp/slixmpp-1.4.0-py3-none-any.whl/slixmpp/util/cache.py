"""
    Slixmpp: The Slick XMPP Library
    Copyright (C) 2018 Emmanuel Gil Peyrot
    This file is part of Slixmpp.

    See the file LICENSE for copying permission.
"""

import os
import logging

log = logging.getLogger(__name__)

class Cache:
    def retrieve(self, key):
        raise NotImplementedError

    def store(self, key, value):
        raise NotImplementedError

class PerJidCache:
    def retrieve_by_jid(self, jid, key):
        raise NotImplementedError

    def store_by_jid(self, jid, key, value):
        raise NotImplementedError

class MemoryCache(Cache):
    def __init__(self):
        self.cache = {}

    def retrieve(self, key):
        return self.cache.get(key, None)

    def store(self, key, value):
        self.cache[key] = value
        return True

class MemoryPerJidCache(PerJidCache):
    def __init__(self):
        self.cache = {}

    def retrieve_by_jid(self, jid, key):
        cache = self.cache.get(jid, None)
        if cache is None:
            return None
        return cache.get(key, None)

    def store_by_jid(self, jid, key, value):
        cache = self.cache.setdefault(jid, {})
        cache[key] = value
        return True

class FileSystemStorage:
    def __init__(self, encode, decode, binary):
        self.encode = encode if encode is not None else lambda x: x
        self.decode = decode if decode is not None else lambda x: x
        self.read = 'rb' if binary else 'r'
        self.write = 'wb' if binary else 'w'

    def _retrieve(self, directory, key):
        filename = os.path.join(directory, key.replace('/', '_'))
        try:
            with open(filename, self.read) as cache_file:
                return self.decode(cache_file.read())
        except FileNotFoundError:
            log.debug('%s not present in cache', key)
        except OSError:
            log.debug('Failed to read %s from cache:', key, exc_info=True)
            return None

    def _store(self, directory, key, value):
        filename = os.path.join(directory, key.replace('/', '_'))
        try:
            os.makedirs(directory, exist_ok=True)
            with open(filename, self.write) as output:
                output.write(self.encode(value))
                return True
        except OSError:
            log.debug('Failed to store %s to cache:', key, exc_info=True)
            return False

class FileSystemCache(Cache, FileSystemStorage):
    def __init__(self, directory, cache_type, *, encode=None, decode=None, binary=False):
        FileSystemStorage.__init__(self, encode, decode, binary)
        self.base_dir = os.path.join(directory, cache_type)

    def retrieve(self, key):
        return self._retrieve(self.base_dir, key)

    def store(self, key, value):
        return self._store(self.base_dir, key, value)

class FileSystemPerJidCache(PerJidCache, FileSystemStorage):
    def __init__(self, directory, cache_type, *, encode=None, decode=None, binary=False):
        FileSystemStorage.__init__(self, encode, decode, binary)
        self.base_dir = os.path.join(directory, cache_type)

    def retrieve_by_jid(self, jid, key):
        directory = os.path.join(self.base_dir, jid)
        return self._retrieve(directory, key)

    def store_by_jid(self, jid, key, value):
        directory = os.path.join(self.base_dir, jid)
        return self._store(directory, key, value)
