from flask import Blueprint, jsonify, request
from utils.db_handler import MongoHandler
from dotenv import load_dotenv
from decorators.authenticated_request import authenticated
from utils.llm_core import LLMCore
import os

env = os.getenv("ENV", "development")

load_dotenv(".env.production" if (env == "production") else ".env.development")

title: str = "post_conversation"
blueprint: Blueprint = Blueprint(title, title)

db: MongoHandler = MongoHandler(uri=os.getenv("MONGODB_URI"))
llm: LLMCore = LLMCore(api_key=os.getenv("OPENAI_API_KEY"))

@blueprint.post("/conversations/")
@authenticated()
def create_conversation(user_id: str):
    """
    Creates a new conversation in the database.
    Returns: JSON with status and conversation_id.
    """

    try:
        req_json: dict = request.get_json()
        webpage_content: str = req_json["webpage_content"]

        # Webpage content missing
        if not webpage_content: return jsonify({
            "status": "fail",
            "error": "Webpage content missing!"
        }), 400
        
        # Generate prompt suggestions
        suggestions: list[str] = llm.prompt_suggestions(webpage_content=webpage_content)
        
        # Create conversation in Database
        conversation_id = db.new_conversation(user_id, suggestions)

        return jsonify({
            "status": "ok",
            "conversation_id": str(conversation_id)
        }), 200

    except Exception as e:
        print(e)
        return jsonify({
            "status": "fail",
            "error": "Internal server error"
        }), 500
