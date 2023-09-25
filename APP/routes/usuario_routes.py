from flask import Blueprint
from ..models.usuario_model import Usuario
from ..database import DatabaseConnection

Usuario_bp = Blueprint('Usuario', __name__)

