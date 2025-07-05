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

        try:
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
                    "type": type,
                    "google_sub": google_sub,
                    "session_token": session_token,
                    "email": email
                })
                
                return f"{str(result.inserted_id)}:{session_token}"

        except Exception: raise Exception
        
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
