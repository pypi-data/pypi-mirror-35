from libaloha.cache import AbstractCache
from libaloha.cache.exceptions import CacheConnectionError
from redis import StrictRedis
from redis.exceptions import ConnectionError
from typing import Any

import logging

logger = logging.getLogger(__name__)


class RedisCache(AbstractCache):

    def __init__(self, host: str = 'localhost', port: int = 6379,
                 db: int = 0, prefix: str = None):
        """
        Cache initialisation
        :param host:
        :param port:
        :param db:
        :param prefix:
        :return:
        """
        self._cache = StrictRedis(host=host, port=port, db=db)
        self._prefix = prefix

        # We do a first request to check if server is up
        try:
            self._cache.exists('null')
        except ConnectionError:
            error_msg = "Connection to redis server {}:{} failed".format(host, port)
            raise CacheConnectionError(error_msg)

    def get_key(self, key: str) -> str:
        """
        Return correct key with prefix
        :param key:
        :return:
        """
        if key.startswith(self._prefix):
            return key
        return self._prefix + key

    def exists(self, key: str) -> bool:
        """
        Return true if a key exists in the cache or false if it doesn't
        :param key:
        :return:
        """
        key = self.get_key(key)
        if key in self._cache:
            return True

        logger.debug("Key not found: {}".format(key))
        return False

    def get(self, key: str) -> Any:
        """
        Return a value from the cache
        :param key:
        :return:
        """
        key = self.get_key(key)
        if self.exists(key):
            result = self._cache.get(key).decode()
            logger.debug("Get {}".format(key))
            return result

    def set(self, key: str, content: Any):
        """
        Set a value in the cache
        :param key:
        :param content:
        :return:
        """
        key = self.get_key(key)
        result = self._cache.set(key, content)
        logger.debug("Set {}".format(key))
        return result

    def remove(self, key: str):
        """
        Delete a value from the cache
        :param key:
        :return:
        """
        key = self.get_key(key)
        if self.exists(key):
            result = self._cache.delete(key)
            logger.debug("Delete '{}".format(key))
            return result
