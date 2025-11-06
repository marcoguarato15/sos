from ..models.usuario_model import Usuario
from app import db

def get_usuarios():
    usuarios = Usuario.query.all()
    return usuarios