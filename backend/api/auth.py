from flask import Blueprint, request, jsonify, make_response
from utils.db_handler import MongoHandler
from datetime import timedelta

title: str="auth"
blueprint:Blueprint=Blueprint(title, __name__)
db:MongoHandler=MongoHandler()

@blueprint.post("/auth/google")
def auth_endpoint():
    """
    register user using Google credential payload and cookie with auth token
    """
    
    try:
        data=request.get_json(force=True)
        user_type:str=data.get("type")
        google_sub:str=data.get("google_sub")

        if not user_type or not google_sub:
            return jsonify({"status": "fail", "error": "Missing 'type' or 'google_sub fields'"}), 400

        #register,auth_token
        auth_token=db.register_google_user(user_type, google_sub)

        #response
        response = make_response(jsonify({"status": "ok"}), 200)
        response.set_cookie(
            "auth_token",
            value=auth_token,
            httponly=True,
            secure=True,
            samesite="Lax",
            max_age=7*24*60*60
        )
        return response

    except Exception as e:
        return jsonify({
            "status": "fail",
            "error": str(e)
        }), 500
