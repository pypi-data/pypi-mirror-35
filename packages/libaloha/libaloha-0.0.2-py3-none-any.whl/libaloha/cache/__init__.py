

class AbstractCache:
    def exists(self, path):
        raise NotImplementedError(self.__class__.__name__)

    def get(self, path):
        raise NotImplementedError(self.__class__.__name__)

    def set(self, path, article):
        raise NotImplementedError(self.__class__.__name__)

    def remove(self, path):
        raise NotImplementedError(self.__class__.__name__)


from .exceptions import CacheException, CacheConnectionError
from .redis import RedisCache

__all__ = ['AbstractCache', 'CacheException', 'CacheConnectionError', 'RedisCache']