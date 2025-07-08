import secrets
from pymongo import MongoClient, errors


class MongoHandler:
    """
    Handles MongoDB operations.
    """
    
    _instance = None
    db = None

    def __new__(cls, uri):
        if cls._instance is None:
            cls._instance = super(MongoHandler, cls).__new__(cls)
            cls._client = MongoClient(uri)
            cls.db = cls._client["askage"]
            
        return cls._instance
    
    def generate_session_token(self) -> str:
        """
        Generates a unique session token.
        """
        return secrets.token_hex(16)
    
    def register_google_user(
        self,
        google_sub: str,
        email: str
    ) -> str:
        """
        Adds user details to registered users in Database.
        Returns: auth_token
        """

        if not google_sub or not email: raise Exception

        collection = self.db["users"]
        session_token = self.generate_session_token()

        existing_user = collection.find_one({"google_sub": google_sub})

        if existing_user:
            collection.update_one(
                {"_id": existing_user["_id"]},
                {"$set": {"session_token": session_token, "email": email}}
            )
            
            return f"{str(existing_user['_id'])}:{session_token}"
        
        else:
            result = collection.insert_one({
                "google_sub": google_sub,
                "session_token": session_token,
                "email": email
            })
            
            return f"{str(result.inserted_id)}:{session_token}"
        
    def new_conversation(
        self,
        user_id: str
    ) -> str:
        """
        Creates a new conversation in Database.
        Returns: conversation_id
        """
        
        try:
            collection = self.db["conversations"]
            result = collection.insert_one({"user_id": user_id})
            
            return str(result.inserted_id)
        
        except Exception as e:
            raise Exception(f"MongoDB error: {e}")
        
    
    def verify_auth_token(self, user_id: ObjectId, session_token: str) -> bool:
        """
        Verifies if the provided session token is valid for the given user.
        """
        try:
            collection = self.db["users"]
            user_doc = collection.find_one({"_id": user_id})

            if not user_doc:
                return False

            return user_doc.get("session_token") == session_token

        except errors.PyMongoError as e:
            raise Exception(f"Database error: {str(e)}")
        except Exception as e:
            raise Exception(f"Unexpected error: {str(e)}")
