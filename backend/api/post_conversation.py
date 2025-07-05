from flask import Blueprint, jsonify
from utils.db_handler import MongoHandler
from dotenv import load_dotenv
import os

env = os.getenv("ENV", "development")

if env == "production":
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env.production"))
else:
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env.development"))


title: str = "post_conversation"
blueprint: Blueprint = Blueprint(title, title)

db: MongoHandler = MongoHandler(uri=os.getenv("MONGODB_URI"))

@blueprint.post("/conversations/")
def create_conversation():
    """
    Creates a new conversation in the database.
    Returns: JSON with status and conversation_id.
    """
    try:
        user_id = "00000"  # sample user ID
    
        conversation_id = db.new_conversation(user_id)

        return jsonify({
            "status": "ok",
            "conversation_id": str(conversation_id)
        }), 200

    except Exception as e:
        return jsonify({
            "status": "fail",
            "error": str(e)
        }), 500
