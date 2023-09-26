from flask import Blueprint
from ..controllers.chat_controller import ChatController
from ..database import DatabaseConnection

Chat_bp = Blueprint('Chat', __name__)

Chat_bp.route('/')(ChatController.index)