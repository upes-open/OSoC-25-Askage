from flask import Blueprint

title: str = "ping"
blueprint: Blueprint = Blueprint(title, title)

@blueprint.get("/ping/")
def endpoint():
    """
    Checks backend and MongoDB connection.
    """
    
    return "", 204
