#from config import Config
from flask import Flask, render_template, request
from controllers.chat_controller import ChatController

app = Flask(__name__)
def init_app():
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api/chat', methods=['GET'])
    def get_chat_messages():
        messages = ChatController.get_chat_messages()
        return messages

    @app.route('/api/chat', methods=['POST'])
    def chat():
        message = request.json.get('message')
        ChatController.save_message(message)
        return jsonify({'status': 'success'})

    return app