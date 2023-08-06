from pymongo import MongoClient
from oceandb_driver_interface.utils import get_value
_DB_INSTANCE = None


def get_database_instance(config_file=None):
    global _DB_INSTANCE
    if _DB_INSTANCE is None:
        _DB_INSTANCE = MongoInstance(config_file)

    return _DB_INSTANCE


class MongoInstance(object):

    def __init__(self, config=None):
        host = get_value('db.hostname', 'DB_HOSTNAME', 'localhost', config)
        port = int(get_value('db.port', 'DB_PORT', 27017, config))
        db_name = get_value('db.name', 'DB_NAME', 'db_name', config)
        collection = get_value('db.collection', 'DB_COLLECTION', 'collection_name', config)
        username = get_value('db.username', 'DB_USERNAME', None, config)
        password = get_value('db.password', 'DB_PASSWORD', None, config)
        self._client = MongoClient(host=host, port=port)
        self._db = self._client[db_name]
        if username is not None and password is not None:
            print('username/password: %s, %s' % (username, password))
            self._db.authenticate(name=username, password=password)

        self._collection = self._db[collection]

    @property
    def instance(self):
        return self._collection
