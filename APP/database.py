import mysql.connector

class DatabaseConnection:
    _connection = None
    
    @classmethod
    def get_connection(cls):
        if cls._connection is None:
            cls._connection = mysql.connector.connect(
                host = '172.17.0.3',
                user = 'root',
                port = '3306',
                password = '1127As305001.',
                database = 'chat'
            )
        return cls._connection
    
    @classmethod
    def execute_query(cls, query, params=None):
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        cursor.close()
    
    @classmethod
    def fetch_one(cls, query, params=None):
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchone()
        cursor.close()
        return result
    
    @classmethod
    def fetch_all(cls, query, params=None):
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result