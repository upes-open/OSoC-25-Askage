from flask import Flask
from dotenv import load_dotenv
import os
from api import ping
from api import post_conversation
from api import auth


load_dotenv()

# Configurations
DEBUG: bool = (os.getenv("DEBUG") == "true")

# Root server
app: Flask = Flask(__name__)

# Register blueprints
app.register_blueprint(ping.blueprint, url_prefix="/api")
app.register_blueprint(post_conversation.blueprint, url_prefix="/api")
app.register_blueprint(auth.blueprint, url_prefix='/api')

# Run development server
if DEBUG:
    app.run(
        debug=DEBUG,
        host="0.0.0.0",
        port=80
    )