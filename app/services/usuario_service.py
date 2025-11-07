from ..models.usuario_model import Usuario
from sqlalchemy.orm import joinedload
from app import db

def get_usuarios():
    usuarios = Usuario.query.options(
        joinedload(Usuario.setor),
        joinedload(Usuario.horario_trabalho)
    ).all()
    return usuarios

def get_usuario_by_email(email):
    usuario = Usuario.query.filter_by(email=email).first()
    return usuario

def get_usuario_by_id(id):
    usuario = Usuario.query.filter_by(id=id).first()
    return usuario