from flask import Blueprint, request, jsonify
from bson import ObjectId
from utils.db_handler import MongoHandler

title: str = "authenticated"
blueprint: Blueprint = Blueprint(title, title)

# Global MongoDB handler
db = MongoHandler("mongodb://localhost:27017/")

@blueprint.get("/authenticated")
def check_authentication():
    """
    Verifies the user's auth token from Authorization header.
    Expected format: Bearer <user_id>:<session_token>
    """
    try:
        auth_header = request.headers.get("Authorization", "")
        
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or malformed Authorization header"}), 401

        auth_token = auth_header.replace("Bearer ", "").strip()
        
        if ":" not in auth_token:
            return jsonify({"error": "Invalid auth_token format"}), 401

        user_id, session_token = auth_token.split(":", 1)

        try:
            user_id = ObjectId(user_id)
            
        except Exception:
            return jsonify({"error": "Invalid user ID format"}), 401

        if db.verify_auth_token(user_id, session_token):
            return jsonify({"status": "ok"}), 200
        else:
            return jsonify({"error": "Unauthorized"}), 401

    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500
