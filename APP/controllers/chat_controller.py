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
        return Mensaje
        # return {'message': mensaje.contenido}, 200
    
    @classmethod
    def index(cls):
        messages = cls.get_chat_messages()
        return render_template('index.html', messages=messages)
    
    @classmethod
    def get_chat_messages(cls):
        query = "SELECT contenido FROM db_sqadchat.mensajes"
        result = DatabaseConnection.fetch_all(query)
        messages = [row[0] for row in result]
        return messages
    
    @classmethod
    def chat(cls):
        message = request.json.get('message')
        cls.save_message(message)
        return jsonify({'status': 'success'})
    
    @classmethod
    def save_message(cls, Mensaje):
        query = "INSERT INTO db_sdqadchat.mensajes (contenido, fecha_envio, ID_usuario, ID_canal) VALUES (%s, %s, %s, %s)"
        mensaje = cls.crear_mensaje(Mensaje)
        params = (Mensaje.contenido, Mensaje.fecha_envio, Mensaje.Id_usuario, Mensaje.ID_canal)
        id = DatabaseConnection.execute_query(query, params)
        return id