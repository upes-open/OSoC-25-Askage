from flask import jsonify
from flask_limiter.errors import RateLimitExceeded

def register_error_handlers(app):
    @app.errorhandler(RateLimitExceeded)
    def handle_rate_limit_error(e):
        return jsonify({
            "error": "Too Many Requests",
            "message": "You have exceeded the allowed number of requests. Please wait and try again later."
        }), 429
