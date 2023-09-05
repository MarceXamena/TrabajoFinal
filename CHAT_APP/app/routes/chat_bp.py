from flask import Blueprint, jsonify, request
from app.database import DatabaseConnection

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/messages', methods=['GET'])
def get_messages():
    query = "SELECT * FROM messages"
    result = DatabaseConnection.fetch_all(query)

    messages = []
    for (id, sender, message) in result:
        messages.append({"id": id, "sender": sender, "message": message})

    return jsonify(messages)

@chat_bp.route('/messages', methods=['POST'])
def create_message():
    data = request.get_json()
    sender = data.get('sender')
    message = data.get('message')

    query = "INSERT INTO messages (sender, message) VALUES (%s, %s)"
    values = (sender, message)
    DatabaseConnection.execute_query(query, values)

    return jsonify({"message": "Mensaje agregado correctamente"})

@chat_bp.route('/messages/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    query = "DELETE FROM messages WHERE id = %s"
    value = (message_id,)
    DatabaseConnection.execute_query(query, value)

    return jsonify({"message": f"Mensaje con ID {message_id} eliminado correctamente"})