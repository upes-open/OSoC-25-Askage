from pymongo import MongoClient

class MongoHandler:
    _instance = None
    _db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoHandler, cls).__new__(cls)
            cls._client = MongoClient("mongodb://localhost:27017/")
            cls._db = cls._client["askage"]
        return cls._instance

    def get_db(self):
        return self._db

# Global variable to access the askage DB
db = MongoHandler().get_db()
