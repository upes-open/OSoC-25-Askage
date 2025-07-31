from flask import Blueprint, jsonify
from utils.db_handler import MongoHandler
from dotenv import load_dotenv
from decorators.authenticated_request import authenticated
import os

env = os.getenv("ENV", "development")

load_dotenv(".env.production" if (env == "production") else ".env.development")

title: str = "get_prompt_suggestions"
blueprint: Blueprint = Blueprint(title, title)

db: MongoHandler = MongoHandler(uri=os.getenv("MONGODB_URI"))

@blueprint.get("/conversations/<conversation_id>/suggestions/")
@authenticated()
def get_prompt_suggestions(user_id: str, conversation_id: str):
    """
    Generates or fetches pre-existing prompt suggestions for current conversation.
    """

    # Validate conversation exists
    if not db.verify_conversation(
        user_id=user_id,
        conversation_id=conversation_id
    ): return jsonify({
        "status": "ok",
        "response": "Conversation not found!"
    })
    
    try:
        # Fetch prompt suggestions
        suggestions: list[str] = db.get_prompt_suggestions(
            user_id=user_id,
            conversation_id=conversation_id
        )
        
        # Validate suggestions list
        if not suggestions:
            return jsonify({
                "status": "fail",
                "error": "Couldn't fetch prompt suggestions. Please re-create the conversation."
            }), 500
            
        # Return prompt suggestions
        return jsonify({
            "status": "ok",
            "suggestions": suggestions
        })
    
    except Exception:
        return jsonify({
            "status": "fail",
            "error": "Something went wrong!"
        }), 500
