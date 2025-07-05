from flask import Blueprint, request, jsonify, make_response
from utils.db_handler import MongoHandler

title: str = "google_auth"
blueprint: Blueprint = Blueprint(title, __name__)
db: MongoHandler = MongoHandler()

@blueprint.post("/auth/google")
def google_auth():
    """
    Register user using google credentials.
    """
    
    try:
        data = request.get_json()
        credential: str = data.get("credential")

        # Invalid credential
        if not credential:
            return jsonify({
                "status": "fail",
                "error": "Missing 'credential' key"
            }), 400

        # Verify credential
        google_sub: str = verify_credential(credential)

        # Register user in database
        auth_token = db.register_google_user("google", google_sub)

        # Return response
        return jsonify({
            "status": "ok",
            "auth_token": auth_token
        }), 200

    # Error
    except Exception as e:
        return jsonify({
            "status": "fail",
            "error": "Something went wrong!"
        }), 500

def verify_credential(credential: str) -> str:
    """
    Verifies if the google credential is valid.
    Returns: google_sub (unique for every google user)
    """
    
    # TODO: Implement
    return "1234"
