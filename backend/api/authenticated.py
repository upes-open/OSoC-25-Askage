from flask import Blueprint, Response
from decorators.authenticated_request import authenticated

title: str = "authenticated"
blueprint: Blueprint = Blueprint(title, title)

@blueprint.get("/authenticated")
@authenticated(allow_unauthenticated=True)
def check_authentication(user_id: str):
    """
    Verifies if request is authenticated.
    """
    
    return Response("", status=200 if user_id else 401)
