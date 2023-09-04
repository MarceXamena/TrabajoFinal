from config import Config
from flask import Flask, render_template, request, jsonify
from .database import DatabaseConnection

app = Flask(__name__)
def init_app():
    @app.route('/')
    def index():
        messages = get_chat_messages()
        return render_template('index.html', messages=messages)

    @app.route('/api/chat', methods=['POST'])
    def chat():
        message = request.json.get('message')
        save_message(message)
        return jsonify({'status': 'success'})

    def get_chat_messages():
        query = "SELECT message FROM chat_messages"
        result = DatabaseConnection.fetch_all(query)
        messages = [row[0] for row in result]
        return messages

    def save_message(message):
        query = "INSERT INTO chat_messages (message) VALUES (%s)"
        params = (message,)
        DatabaseConnection.execute_query(query, params)

    return app