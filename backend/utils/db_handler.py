from pymongo import MongoClient


class MongoHandler:
    """
    Handles MongoDB operations.
    """
    
    _instance = None
    db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoHandler, cls).__new__(cls)
            cls._client = MongoClient("mongodb://localhost:27017/")
            cls.db = cls._client["askage"]
            
        return cls._instance
