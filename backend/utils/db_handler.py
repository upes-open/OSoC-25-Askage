import secrets
from pymongo import MongoClient, errors


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
    
    def generate_session_token(self) -> str:
        """
        Generates a unique session token.
        """
        return secrets.token_hex(16)
    
    def register_google_user(
        self,
        type: str,
        google_sub: str
    ) -> str:
        """
        Adds user details to registered users in Database.
        Returns: auth_token
        """

        try:
            if not type or not google_sub:
                raise Exception("Both 'type' and 'google_sub' must be provided.")

            collection = self.db["users"]
            session_token = self.generate_session_token()

            existing_user = collection.find_one({"google_sub": google_sub})

            if existing_user:
                collection.update_one(
                    {"_id": existing_user["_id"]},
                    {"$set": {"session_token": session_token}}
                )
                return f"{str(existing_user['_id'])}:{session_token}"
            else:
                result = collection.insert_one({
                    "type": type,
                    "google_sub": google_sub,
                    "session_token": session_token
                })
                return f"{str(result.inserted_id)}:{session_token}"

        except errors.PyMongoError as e:
            raise Exception(f"MongoDB error: {e}")
        except Exception as e:
            raise Exception(f"Error: {e}")
        
    def new_conversation(
        self,
        user_id: str
    ) -> str:
        """
        Creates a new conversation in Database.
        Returns: conversation_id
        """

        # Use `self.db`
        
        # TODO: Must return conversation id (that's the _id of document just created)
