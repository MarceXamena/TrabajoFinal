from flask import Blueprint
from ..models.models import Usuario
from ..database import DatabaseConnection

Usuario_bp = Blueprint('Usuario', __name__)


