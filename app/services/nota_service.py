from app import db
from app.models.nota_model import Nota

def get_notas():
    notas = Nota.query.filter_by(ativo=True).all()
    return notas

def post_nota(nota):
    n = Nota(titulo=nota.titulo, demanda_id=nota.demanda_id, prioridade_id=nota.prioridade_id, data_criacao=nota.data_criacao, ativo=True)
    db.session.add(n)
    db.session.commit()
