from flask import Blueprint, jsonify
from mongo_handler import db

title: str = "ping"
blueprint: Blueprint = Blueprint(title, title)

@blueprint.get("/ping/")
def endpoint():
    """
    Checks backend and MongoDB connection.
    """
    try:
        collections = db.list_collection_names()
        return jsonify({
            "message": "Pong!",
            "mongo_collections": collections
        }), 200

    except Exception as e:
        return jsonify({
            "message": "MongoDB connection failed",
            "error": str(e)
        }), 500
