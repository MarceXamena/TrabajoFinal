from ..models.usuario_model import Usuario
from flask import request

class UsuarioController:
    @classmethod
    def crear_usuario(self):
        usuario = Usuario(
            nombre = request.args.get('nombre', ''),
            correo_electronico = request.args.get('correo_electronico', ''),
            contrasena = request.args.get('contrasena', ''),
            foto_perfil = request.args.get('foto_perfil', '')
        )
        
        Usuario.crear_usuario(Usuario)
        return {'message': 'Usuario creado con éxito'}, 200