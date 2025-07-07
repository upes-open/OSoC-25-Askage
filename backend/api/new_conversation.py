from flask import Blueprint, request, jsonify
from utils.db_handler import MongoHandler
from dotenv import load_dotenv
import os

env = os.getenv("ENV", "development")

if env == "production":
    dotenv_path = os.path.join(os.path.dirname(__file__), "../.env.prodexample")
else:
    dotenv_path = os.path.join(os.path.dirname(__file__), "../.env.development")

load_dotenv(dotenv_path=dotenv_path)

title: str = "new_conversation"
blueprint: Blueprint = Blueprint(title, __name__)
db: MongoHandler = MongoHandler(uri=os.getenv("MONGODB_URI"))

@blueprint.post("/conversation/new")
def new_conversation():
    """
    Creates a new conversation for a user.
    """
    try:
        data = request.get_json()
        user_id: str = data.get("user_id")

        if not user_id:
            return jsonify({
                "status": "fail",
                "error": "Missing 'user_id' in request"
            }), 400

        conversation_id = db.new_conversation(user_id)

        return jsonify({
            "status": "ok",
            "conversation_id": str(conversation_id)
        }), 200

    except Exception as e:
        print(f"Error creating conversation: {e}")
        return jsonify({
            "status": "fail",
            "error": "Something went wrong!"
        }), 500