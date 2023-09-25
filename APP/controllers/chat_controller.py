from ..models.chat_model import Mensaje
from flask import request

class ChatController:
    @classmethod
    def crear_mensaje(self):
        mensaje = Mensaje(
            contenido = request.args.get('contenido', ''),
            fecha_envio = request.args.get('fecha_envio', ''),
            ID_usuario = request.args.get('ID_usuario', ''),
            ID_canal = request.args.get('ID_canal', '')
        )
        
        Mensaje.crear_mensaje(Mensaje)
        return {'message': mensaje.contenido}, 200