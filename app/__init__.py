# app/__init__.py
from flask import Flask
from flask_cors import CORS  # Import CORS to handle Cross-Origin Resource Sharing
from app.routes import main  # Import the main Blueprint
from app.endpoints import api  # Import the API Blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # Load configurations from config.py

    # Enable CORS for all routes (you can restrict to specific origins if needed)
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
    # CORS(app)

    # Register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')

    return app
