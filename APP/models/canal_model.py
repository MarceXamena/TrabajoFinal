from ..database import DatabaseConnection

class Canal:
    def __init__(self, ID_canal = None, nombre = None, descripcion = None, fecha_creacion = None, ID_servidor = None):
        self.ID_Mensaje = ID_canal
        self.contenido = nombre
        self.fecha_envio = descripcion
        self.ID_usuario = fecha_creacion
        self.ID_canal = ID_servidor

