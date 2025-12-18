from app import db
from app.models.tarefa_model import Tarefa

def get_tarefas():
    tarefas = Tarefa.query.filter_by(ativo=True).all()
    return tarefas

def get_tarefa_by_id(id):
    tarefa = Tarefa.query.filter_by(id=id).first()
    return tarefa

def post_tarefa(tarefa):
    # tarefa = Tarefa(titulo, descricao, prioridade_tarefa_id, status_tarefa_id)
    tarefa_obj = Tarefa(titulo=tarefa.titulo, descricao=tarefa.descricao, prioridade_tarefa_id=tarefa.prioridade_tarefa_id, status_tarefa_id=tarefa.status_tarefa_id, data_criacao=tarefa.data_criacao, ativo=True)
    db.session.add(tarefa_obj)
    db.session.commit()


def del_tarefa(id):
    tarefa = Tarefa.query.filter_by(id=id).first()
    tarefa.ativo = False
    db.session.commit()
    return tarefa