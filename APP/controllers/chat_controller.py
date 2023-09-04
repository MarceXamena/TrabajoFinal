from flask import jsonify
from models.message import Message

class ChatController:
    @staticmethod
    def get_chat_messages():
        messages = Message.get_all()
        return jsonify(messages)
    
    @staticmethod
    def save_message(message):
        Message.create(message)
        return jsonify({'status': 'success'})