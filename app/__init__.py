# app/__init__.py
from flask import Flask
from flask_cors import CORS  # Import CORS to handle Cross-Origin Resource Sharing
from app.routes import main  # Import the main Blueprint
from app.endpoints import api  # Import the API Blueprint
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # Enable CORS for all routes (you can restrict to specific origins if needed)
    # CORS(app, resources={r"/api/*": {"origins": os.environ.get("FRONTEND_DOMAIN")}})
    CORS(app)

    # Register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')

    return app
