from flask import Blueprint
from ..controllers.chat_controller import ChatController
# from ..database import DatabaseConnection

Chat_bp = Blueprint('Chat', __name__)

Chat_bp.route('/', methods=['POST'])(ChatController.index)
Chat_bp.route('/api/chat', methods=['POST'])(ChatController.chat)
Chat_bp.route('/mensaje', methods=['GET'])(ChatController.get_message)
Chat_bp.route('/nuevo', methods=['POST'])(ChatController.save_message)