from app import db
from ..models.setor_model import Setor
from datetime import datetime

def get_setores():
    setores = Setor.query.filter_by(ativo=True).all()
    return setores

def get_setor_by_id(id):
    setor = Setor.query.filter_by(id=id).first()
    return setor

def post_setor(setor):
    s = Setor(nome=setor.nome, gestor_id=setor.gestor_id, ativo=setor.ativo, data_criacao=setor.data_criacao)
    db.session.add(s)
    db.session.commit()

def put_setor(id, nome, gestor_id):
    setor = get_setor_by_id(id)
    setor.nome = nome
    setor.gestor_id = gestor_id
    setor.data_atualizacao = datetime.now()
    db.session.commit()
    return setor

def del_setor(id):
    setor = get_setor_by_id(id)
    setor.ativo = False
    setor.data_atualizacao = datetime.now()
    db.session.commit()