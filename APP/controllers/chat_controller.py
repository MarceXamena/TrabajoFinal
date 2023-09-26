from ..models.chat_model import Mensaje
from flask import render_template, request, jsonify
from ..database import DatabaseConnection

class ChatController:
    @classmethod
    def crear_mensaje(cls):
        contenido = request.args.get('contenido', '')
        fecha_envio = request.args.get('fecha_envio', '')
        ID_usuario = request.args.get('ID_usuario', '')
        ID_canal = request.args.get('ID_canal', '')
        

        mensaje = Mensaje(contenido=contenido, fecha_envio=fecha_envio, ID_usuario=ID_usuario, ID_canal=ID_canal)
        
        # Llamar al método
        Mensaje.crear_mensaje(Mensaje)
        return {'message': mensaje.contenido}, 200
    
    @classmethod
    def index(cls):
        messages = cls.get_chat_messages()
        return render_template('index.html', messages=messages)
    
    @classmethod
    def get_chat_messages(cls):
        query = "SELECT message FROM chat_messages"
        result = DatabaseConnection.fetch_all(query)
        messages = [row[0] for row in result]
        return messages
    
# @app.route('/')
#     

#     @app.route('/api/chat', methods=['POST'])
#     def chat():
#         message = request.json.get('message')
#         save_message(message)
#         return jsonify({'status': 'success'})

#     def get_chat_messages():
#         query = "SELECT message FROM chat_messages"
#         result = DatabaseConnection.fetch_all(query)
#         messages = [row[0] for row in result]
#         return messages

#     def save_message(message):
#         query = "INSERT INTO chat_messages (message) VALUES (%s)"
#         params = (message,)
#         DatabaseConnection.execute_query(query, params)