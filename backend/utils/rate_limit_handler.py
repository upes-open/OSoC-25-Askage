from flask import jsonify
from flask_limiter.errors import RateLimitExceeded

def register_rate_limit_handler(app):
    @app.errorhandler(RateLimitExceeded)
    def handle_rate_limit_error(e):
        return jsonify({
            "status": "fail",
            "message": "You sent too many requests. Please slow down!"
        }), 429
