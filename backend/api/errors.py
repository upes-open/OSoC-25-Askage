from flask import Blueprint, jsonify

title: str = "errors"
blueprint: Blueprint = Blueprint(title, __name__)

@blueprint.app_errorhandler(404)
def handle_404(e):
    """
    custom handler for 404 error
    """
    return jsonify({
        "status": "ok",
        "error": "This endpoint doesn't exist"
    }), 404
