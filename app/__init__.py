# app/__init__.py
from flask import Flask
from app.routes import main  # Import the main Blueprint
from app.endpoints import api  # Import the API Blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # Load configurations from config.py

    # Register Blueprints
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')

    return app
