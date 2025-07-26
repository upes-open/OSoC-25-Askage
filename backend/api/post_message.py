from flask import Blueprint, request, jsonify
from utils.db_handler import MongoHandler
from dotenv import load_dotenv
from decorators.authenticated_request import authenticated
import os
from utils.llm_core import LLMCore

env = os.getenv("ENV", "development")

load_dotenv(".env.production" if (env == "production") else ".env.development")

db: MongoHandler = MongoHandler(uri=os.getenv("MONGODB_URI"))
llm: LLMCore = LLMCore(api_key=os.getenv("OPENAI_API_KEY"))

title: str = "post_message"
blueprint: Blueprint = Blueprint(title, title)

def remove_duplicate_lines(text):
    seen = set()
    result = []
    
    for line in text.splitlines():
        if line not in seen:
            seen.add(line)
            result.append(line)
    
    return '\n'.join(result)

@blueprint.post("/conversations/<conversation_id>/messages/")
@authenticated(allow_unauthenticated=True)
def post_message(user_id: str, conversation_id: str):
    """
    API Endpoint to send a message.
    """
    
    if not user_id or not db.verify_conversation(
        user_id=user_id,
        conversation_id=conversation_id
    ): return jsonify({
        "status": "ok",
        "response": "You're not logged in."
    }), 200
    
    try:
        data = request.get_json()
        message = data.get("message")
        webpage_content = remove_duplicate_lines(data.get("webpage_content"))
        
        # Fetch chat history
        chat_history: list[dict[str, str]] = db.get_chat_history(
            user_id=user_id,
            conversation_id=conversation_id
        )
        
        # Prepare prompt
        prompt_content: str = f"User's prompt: \"{message}\"\nBelow is the text scraped from the user's currently opened webpage. Use it only as context for your response:\n{webpage_content}"
        
        # Generate LLM response
        llm_response: str = llm.prompt([*chat_history, {
            "role": "user",
            "content": prompt_content
        }])
        
        # Prepare new chat history
        modified_chat_history: list[dict[str, str]] = [
            *chat_history,
            {"role": "user", "content": message},
            {"role": "assistant", "content": llm_response}
        ]
        
        # Update chat history in Database
        db.update_chat_history(
            user_id=user_id,
            conversation_id=conversation_id,
            history=modified_chat_history
        )
        
        return jsonify({
            "response": llm_response
        }), 200

    except Exception as e:
        return jsonify({
            "status": "fail",
            "error": "Something went wrong on our side!"
        }), 500
