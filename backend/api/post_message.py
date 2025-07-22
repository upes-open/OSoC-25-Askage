from flask import Blueprint, request, jsonify
from utils.db_handler import MongoHandler
from dotenv import load_dotenv
from decorators.authenticated_request import authenticated
import os

env = os.getenv("ENV", "development")
load_dotenv(".env.production" if env == "production" else ".env.development")

title: str = "post_message"
blueprint: Blueprint = Blueprint(title, title)

db: MongoHandler = MongoHandler(uri=os.getenv("MONGODB_URI"))

@blueprint.post("/conversations/<string:conversation_id>/messages/")
@authenticated()
def post_message(conversation_id: str, user_id: str):
    """
    Endpoint to handle posting a message to a specific conversation.
    Accepts JSON body with keys `message` and `webpage_content`.
    Returns a placeholder response for now.
    """

    try:
        data = request.get_json()

        # Extract fields from request body
        message = data.get("message")
        webpage_content = data.get("webpage_content")

        # ✅ Placeholder for future chat generation logic
        # You can later use `message`, `webpage_content`, and `conversation_id` here

        return jsonify({
            "response": "Hey! I'm Askage. Currently I am not accepting any new requests."
        }), 200

    except Exception as e:
        return jsonify({
            "status": "fail",
            "error": str(e)
        }), 500
      
