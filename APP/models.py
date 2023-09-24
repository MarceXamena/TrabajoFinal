from .database import DatabaseConnection

class Usuario:
    def __init__(self, ID_usuario = None, nombre = None, correo_electronico = None, contrasena = None, foto_perfil = None):
        self.ID_usuario = ID_usuario
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.foto_perfil = foto_perfil

    @classmethod
    def crear_usuario(cls, Usuario):
        query = 'INSERT INTO db_sqadchat.usuarios (ID_usuario, nombre, correo_electronico, contrasena, foto_perfil) VALUES (%s, %s, %s, %s, %s)'
        params = (Usuario.ID_usuario, Usuario.nombre, Usuario.correo_electronico, Usuario.contrasena, Usuario.foto_perfil)
        DatabaseConnection.execute_query(query, params)
    