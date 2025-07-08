from flask import request, jsonify, Response
from utils.db_handler import MongoHandler
from dotenv import load_dotenv
import os

env = os.getenv("ENV", "development")

load_dotenv(".env.production" if (env == "production") else ".env.development")

db: MongoHandler = MongoHandler(uri=os.getenv("MONGODB_URI"))


def authenticated(allow_unauthenticated: bool = False):
    """
    Checks if the request is authenticated.
    
    :param allow_unauthenticated: Should call the origninal function even if request is unauthenticated?
    :param allow_unauthenticated: bool
    """
    
    def decorator(func):
        """
        Decorator to check if the request is authenticated.
        """
        
        def wrapper(*args, **kwargs):
            """
            Wrapper function to check auth status.
            """
            
            user_id: str | None = None
            
            # Parse authorization header
            auth_header: str = request.headers.get("Authorization", "")
            
            # Invalid authorization header
            if not auth_header or not auth_header.startswith("Bearer "):
                return func(None, *args, **kwargs) if allow_unauthenticated else unauthenticated_response()

            # Parse auth token
            auth_token: str = auth_header.replace("Bearer ", "").strip()
            
            # Invalid auth token
            if ":" not in auth_token:
                return func(None, *args, **kwargs) if allow_unauthenticated else unauthenticated_response()
            
            # Parse credentials
            user_id: str = auth_token.split(":", 1)[0]
            session_token: str = auth_token.split(":", 1)[1]
            
            # Verify credentials
            if not db.verify_auth_token(user_id, session_token):
                return func(None, *args, **kwargs) if allow_unauthenticated else unauthenticated_response()
            
            # Call origninal function
            return func(user_id, *args, **kwargs)
        
        return wrapper
    
    return decorator


def unauthenticated_response() -> Response:
    """
    Returns Flask response for unauthenticated requests.
    """
    
    return jsonify({
        "status": "fail",
        "error": "Please sign in again!"
    }), 401
