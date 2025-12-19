from ..models.usuario_model import Usuario
from datetime import datetime
from app import db

def get_usuarios(nome=None):
    query = Usuario.query
    if nome:
        query = query.filter(Usuario.nome.like(f"%{nome}%"))
    
    usuarios = query.filter_by(ativo=True).all()
    
    return usuarios

def get_usuario_by_email(email):
    usuario = Usuario.query.filter_by(email=email).first()
    return usuario

def get_usuario_by_id(id):
    usuario = Usuario.query.filter_by(id=id).first()
    return usuario

def set_ultimo_login(usuario):
    usuario.ultimo_login = datetime.now()
    db.session.commit()

def add_usuario(usuario):
    usr = Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha, cargo=usuario.cargo, setor_id=usuario.setor_id, ativo=usuario.ativo, papel=usuario.papel, disponivel=usuario.disponivel, contato=usuario.contato, criador_id=usuario.criador_id, data_criacao=datetime.now(), horario_trabalho_id=usuario.horario_trabalho_id)

    usr.encriptar_senha()

    db.session.add(usr)
    db.session.commit()

def put_usuario(id_usuario,nome, email, cargo, setor_id, papel, disponivel, contato, horario_trabalho_id, id):
    usuario = get_usuario_by_id(id)
    usuario.id_usuario = id_usuario
    usuario.nome = nome
    usuario.email = email
    usuario.cargo = cargo
    usuario.setor_id = setor_id
    usuario.papel = papel
    usuario.disponivel = disponivel
    usuario.contato = contato
    usuario.horario_trabalho_id = horario_trabalho_id
    usuario.ultima_atualizacao = datetime.now()
    db.session.commit()

    return usuario

def del_usuario(id):
    usuario = get_usuario_by_id(id)
    usuario.ativo = False
    usuario.deletado_em = datetime.now()
    db.session.commit()

def set_ultima_atualizacao(id):
    usuario = get_usuario_by_id(id)
    usuario.ultima_atualizacao = datetime.now()
    db.session.commit()

def set_senha(usuario,senha):
    usr = Usuario(senha=senha)
    usr.encriptar_senha()
    usuario.senha = usr.senha
    db.session.commit()
    
def get_usuario_by_id_usuario(id_usuario):
    usuario = Usuario.query.filter_by(id_usuario=id_usuario).first()
    return usuario