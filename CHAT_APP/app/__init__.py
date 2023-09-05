from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/chat'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Importar los blueprints
    from .routes import chat_bp

    # Registrar los blueprints
    app.register_blueprint(chat_bp)

    return app