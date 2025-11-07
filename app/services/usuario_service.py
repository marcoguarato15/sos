from ..models.usuario_model import Usuario
from app import db

def get_usuarios():
    usuarios = Usuario.query.all()
    return usuarios

def get_usuario_by_email(email):
    usuario = Usuario.query.filter_by(email=email).first()
    return usuario

def get_usuario_by_id(id):
    usuario = Usuario.query.filter_by(id=id).first()
    return usuario