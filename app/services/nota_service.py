from app import db
from app.models.nota_model import Nota
from app.models.demanda_model import Demanda
from sqlalchemy import or_

def get_notas(titulo=None, id_demanda=None, categoria_id=None):
    query = Nota.query
    if titulo:
        query = query.filter(Nota.titulo.like(f"%{titulo}%"))
    if id_demanda:
        query = query.filter(Nota.demanda.has(Demanda.id_demanda.like(f"%{id_demanda}%")))
    if categoria_id:
        query = query.filter(Nota.demanda.has(Demanda.categoria_id == categoria_id))
    
    notas = query.filter_by(ativo=True).all()
    return notas

def get_notas_suspensas():
    notas = Nota.query.filter_by(ativo=False).all()

    return notas

def post_nota(nota):
    n = Nota(titulo=nota.titulo, demanda_id=nota.demanda_id, data_criacao=nota.data_criacao, ativo=nota.ativo)
    db.session.add(n)
    db.session.commit()

def put_nota(id, titulo, demanda_id):
    nota = Nota.query.filter_by(id=id).first()
    nota.titulo = titulo
    nota.demanda_id = demanda_id
    db.session.commit()

def get_nota_by_id(id):
    nota = Nota.query.filter_by(id=id).first()
    return nota

def del_nota(id):
    nota = Nota.query.filter_by(id=id).first()
    nota.ativo = False
    db.session.commit()