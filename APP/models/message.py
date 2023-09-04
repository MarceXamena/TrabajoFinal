from database import DatabaseConnection

class Message:
    @staticmethod
    def get_all():
        query = "SELECT message FROM chat_messages"
        result = DatabaseConnection.fetch_all(query)
        messages = [row[0] for row in result]
        return messages
    
    @staticmethod
    def create(message):
        query = "INSERT INTO chat_messages (message) VALUES (%s)"
        params = (message,)
        DatabaseConnection.execute_query(query, params)