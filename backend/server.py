from flask import Flask
from dotenv import load_dotenv
import os
from api import ping

env = os.getenv("ENV", "development")

if env == "production":
    load_dotenv(".env.prodexample")
else:
    load_dotenv(".env.development")


# Configurations
DEBUG: bool = (os.getenv("DEBUG") == "true")

# Root server
app: Flask = Flask(__name__)

# Register blueprints
app.register_blueprint(ping.blueprint, url_prefix="/api")

# Run development server
if DEBUG:
    app.run(
        debug=DEBUG,
        host="0.0.0.0",
        port=80
    )
