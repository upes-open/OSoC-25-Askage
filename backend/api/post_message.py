from flask import Blueprint, request, jsonify
from dotenv import load_dotenv
from decorators.authenticated_request import authenticated
import os

env = os.getenv("ENV", "development")

load_dotenv(".env.production" if (env == "production") else ".env.development")

title: str = "post_message"
blueprint: Blueprint = Blueprint(title, title)

@blueprint.post("/conversations/<conversation_id>/messages/")
@authenticated()
def post_message(user_id: str, conversation_id: str):
    try:
        data = request.get_json()
        message = data.get("message")
        webpage_content = data.get("webpage_content")

        return jsonify({
            "response": "Hey! I'm Askage. Currently I am not accepting any new requests."
        }), 200

    except Exception as e:
        return jsonify({
            "status": "fail",
            "error": "Something went wrong on our side!"
        }), 500
