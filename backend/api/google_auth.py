from flask import Blueprint, request, jsonify
from utils.db_handler import MongoHandler
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from dotenv import load_dotenv
import requests
from requests import Response
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env"))

GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI: str = os.getenv("GOOGLE_REDIRECT_URI")

title: str = "google_auth"
blueprint: Blueprint = Blueprint(title, __name__)
db: MongoHandler = MongoHandler(uri=os.getenv("MONGODB_URI"))

@blueprint.post("/auth/google")
def google_auth():
    """
    Register user using google credentials.
    """
    
    try:
        data = request.get_json()
        code: str = data.get("code")

        # Invalid credential
        if not code:
            return jsonify({
                "status": "fail",
                "error": "Missing 'credential' key"
            }), 400

        # Verify credential
        google_sub, google_email = verify_credential(code)

        # Register user in database
        auth_token = db.register_google_user(google_sub, google_email)

        # Return response
        return jsonify({
            "status": "ok",
            "auth_token": auth_token
        }), 200

    # Something went wrong
    except Exception:
        return jsonify({
            "status": "fail",
            "error": "Something went wrong!"
        }), 500

def verify_credential(code: str) -> str:
    """
    Verifies if the google credential is valid.
    Returns: google_sub (unique for every google user), email
    """
    
    # Get ID token
    id_token_str: str = get_id_token(code)
    
    id_info: dict = id_token.verify_oauth2_token(
        id_token_str,
        google_requests.Request(),
        audience=GOOGLE_CLIENT_ID,
        clock_skew_in_seconds=5
    )
    
    user_sub: str = id_info["sub"]
    user_email: str = id_info["email"]
    
    return user_sub, user_email

def get_id_token(code: str) -> str:
    """
    Fetches id_token from google code.
    Returns: id_token
    """
    
    token_url: str = "https://oauth2.googleapis.com/token"
    
    data: dict = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    
    response: Response = requests.post(url=token_url, data=data)
    token_info = response.json()

    return token_info["id_token"]
