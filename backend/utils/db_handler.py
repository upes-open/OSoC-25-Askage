import secrets
from pymongo import MongoClient, errors
# from bson import ObjectId
from bson.objectid import ObjectId, InvalidId


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
        
    
    def verify_auth_token(self, user_id: str, session_token: str) -> bool:
        """
        Verifies if the provided session token is valid for the given user.
        """
        
        collection = self.db["users"]
        user_doc = collection.find_one({"_id": ObjectId(user_id)})
        
        return ((user_doc is not None) and (user_doc.get("session_token", "") == session_token))
    def verify_conversation(self, user_id: str, conversation_id: str) -> bool:
        """
        Verifies if the provided session token is valid for the given user.

         Args:
        user_id (str): The ID of the user.
        conversation_id (str): The ID of the conversation to verify.

        Returns:
            bool: True if the conversation exists for the user, False otherwise.

        Raises:
            Exception: If any error occurs or the conversation_id is invalid.
        """
        try:
            conversation_obj_id = ObjectId(conversation_id)
            collection = self.db["conversations"]
            result = collection.find_one({
                "_id": conversation_obj_id,
                "user_id": user_id
            })
            return result is not None
        except (InvalidId, Exception) as e:
            raise Exception(f"MongoDB error: {e}")