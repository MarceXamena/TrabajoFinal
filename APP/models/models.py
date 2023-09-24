from ..database import DatabaseConnection

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
    
    @classmethod
    def get_Usuario(Usuario):
        query = 'SELECT ID_usuario, nombre, correo_electronico, contrasena, foto_perfil FROM db_sqadchat.usuarios WHERE ID_usuario = %s'
        params = Usuario.ID_usuario
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Usuario(
                ID_usuario = Usuario.ID_usuario,
                nombre = Usuario.nombre,
                correo_electronico = Usuario.correo_electronico,
                contrasena = Usuario.contrasena,
                foto_perfil = Usuario.foto_perfil,
            )
        else:
            return None