from flask import Blueprint, jsonify
from utils.db_handler import MongoHandler

title: str = "post_conversation"
blueprint: Blueprint = Blueprint(title, title)

db: MongoHandler = MongoHandler() 

@blueprint.post("/conversations/")
def create_conversation():
    """
    Creates a new conversation in the database for a sample user.
    Returns: JSON with status and conversation_id.
    """
    try:
        user_id = "00000"  # sample user ID
        db = MongoHandler()
        conversation_id = db.new_conversation(user_id)

        return jsonify({
            "status": "ok",
            "conversation_id": str(conversation_id)
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
