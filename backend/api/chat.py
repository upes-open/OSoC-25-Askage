from flask import Blueprint, request, jsonify
from utils.llm_core import LLMCore
import os
from dotenv import load_dotenv
load_dotenv()

blueprint = Blueprint("chat", __name__)

llm = LLMCore(api_key=os.getenv("OPENAI_API_KEY"))

@blueprint.route("/chat/", methods=["POST"])
def chat_endpoint():
    data = request.get_json()
    if not data or "messages" not in data:
        return jsonify({"error": "Missing 'messages' in request body"}), 400

    try:
        updated_chat = llm.prompt(data["messages"])
        return jsonify(updated_chat)
    except Exception as e:
        return jsonify({"error": str(e)}), 500