from app import db
from app.models.tarefa_model import Tarefa

def get_tarefas():
    tarefas = Tarefa.query.filter_by(ativo=True).all()
    return tarefas

def get_tarefa_by_id(id):
    tarefa = Tarefa.query.filter_by(id=id).first()
    return tarefa

def del_tarefa(id):
    tarefa = Tarefa.query.filter_by(id=id).first()
    tarefa.ativo = False
    db.session.commit()
    return tarefa