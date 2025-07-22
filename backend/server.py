from flask import Flask
from dotenv import load_dotenv
import os
from api import ping
from api import post_conversation
from api import google_auth
from api import post_message
from api.errors import blueprint as errors_blueprint
from utils.db_handler import MongoHandler
from utils.limiter import limiter
from utils.rate_limit_handler import register_rate_limit_handler
from api import authenticated
env = os.getenv("ENV", "development")

load_dotenv(".env.production" if (env == "production") else ".env.development")

# Initialize MongoDB
db: MongoHandler = MongoHandler(uri=os.getenv("MONGODB_URI"))

# Configurations
DEBUG: bool = (os.getenv("DEBUG") == "true")

# Root server
app: Flask = Flask(__name__)

# Register Rate Limiter
limiter.init_app(app)

# Register blueprints
app.register_blueprint(ping.blueprint, url_prefix="/api")
app.register_blueprint(post_conversation.blueprint, url_prefix="/api")
app.register_blueprint(post_message.blueprint, url_prefix="/api")
app.register_blueprint(google_auth.blueprint, url_prefix='/api')
app.register_blueprint(authenticated.blueprint, url_prefix="/api")
app.register_blueprint(errors_blueprint)

# Register error handlers
register_rate_limit_handler(app)

# Run development server
if DEBUG:
    app.run(
        debug=DEBUG,
        host="0.0.0.0",
        port=80
    )
