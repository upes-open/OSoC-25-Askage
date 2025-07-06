from flask import Blueprint
from utils.limiter import limiter

title: str = "ping"
blueprint: Blueprint = Blueprint(title, title)

@blueprint.get("/ping/")
@limiter.limit("2 per second")

def endpoint():
    """
    Checks backend and MongoDB connection.
    """
    
    return "", 204
