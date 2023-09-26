from config import Config
from flask import Flask, render_template, request, jsonify
from .routes.chat_routes import Chat_bp


def init_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(Chat_bp, url_prefix='/chat')

    return app