from ..database import DatabaseConnection

class Mensaje:
    def __init__(self, ID_Mensaje = None, contenido = None, fecha_envio = None, ID_usuario = None, ID_canal = None):
        self.ID_Mensaje = ID_Mensaje
        self.contenido = contenido
        self.fecha_envio = fecha_envio
        self.ID_usuario = ID_usuario
        self.ID_canal = ID_canal
        

    # @classmethod
    # def crear_mensaje(cls, Mensaje):
    #     query = 'INSERT INTO db_sqadchat.mensajes (contenido, fecha_envio, ID_usuario, ID_canal) VALUES (%s, %s, %s, %s)'
    #     params = (Mensaje.contenido, Mensaje.fecha_envio, Mensaje.ID_usuario, Mensaje.ID_canal)
    #     DatabaseConnection.execute_query(query, params)
    
    # @classmethod
    # def get_mensaje(Mensaje):
    #     query = 'SELECT ID_Mensaje, contenido, fecha_envio, ID_usuario, ID_canal FROM db_sqadchat.mensajes WHERE ID_Mensaje = %s'
    #     params = Mensaje.ID_Mensaje
    #     result = DatabaseConnection.fetch_one(query, params)
    #     if result is not None:
    #         return Mensaje(
    #             ID_Mensaje = Mensaje.ID_Mensaje,
    #             contenido = Mensaje.contenido,
    #             fecha_envio = Mensaje.fecha_envio,
    #             ID_usuario = Mensaje.ID_usuario,
    #             ID_canal = Mensaje.ID_canal
    #         )
    #     else:
    #         return None
        
        