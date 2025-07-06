# /backend/api/authenticated.py

from flask import Blueprint, request, jsonify
from backend.db.db_manager import MongoHandler

title: str = "authenticated"
blueprint: Blueprint = Blueprint(title, title)

@blueprint.get("/authenticated")
def check_authentication():
    """
    Verifies the user's auth token.
    """
    try:
        auth_header = request.headers.get("Authorization", "")
        if not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or malformed Authorization header"}), 401

        auth_token = auth_header.replace("Bearer ", "").strip()
        if ":" not in auth_token:
            return jsonify({"error": "Invalid auth_token format"}), 401

        user_id, session_token = auth_token.split(":", 1)
        db = MongoHandler()

        if db.verify_auth_token(user_id, session_token):
            return jsonify({"status": "ok"}), 200
        else:
            return jsonify({"error": "Unauthorized"}), 401

    except Exception as e:
        return jsonify({"error": "Internal Server Error", "details": str(e)}), 500
