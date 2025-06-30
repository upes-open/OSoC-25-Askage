from flask import Blueprint

title: str = "ping"
blueprint: Blueprint = Blueprint(title, title)

@blueprint.get("/ping/")
def endpoint():
    """
    Sample endpoint to ping backend server.
    """
    
    return "", 204
