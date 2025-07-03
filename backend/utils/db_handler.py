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
    
    def generate_session_token(self) -> str:
        """
        Generates a unique session token.
        """
        
        # TODO: Return random 32-bit token generated using secrets module.
    
    def register_google_user(
        self,
        type: str,
        google_sub: str
    ) -> str:
        """
        Adds user details to registered users in Database.
        Returns: auth_token
        """

        # Use `self.db`
        
        # TODO: Must return auth_token in format: "<user-id>:<session-token>"
        
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
