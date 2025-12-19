from app import db
from app.models.tarefa_model import Tarefa

def get_tarefas():
    tarefas = Tarefa.query.filter((Tarefa.status_tarefa_id != 16) & (Tarefa.ativo == True)).all()
    return tarefas

def get_tarefas_indeferidas():
    tarefas_indeferidas = Tarefa.query.filter(Tarefa.status_tarefa_id == 16).all()
    return tarefas_indeferidas

def get_tarefa_by_id(id):
    tarefa = Tarefa.query.filter_by(id=id).first()
    return tarefa

def post_tarefa(tarefa):
    # tarefa = Tarefa(titulo, descricao, prioridade_tarefa_id, status_tarefa_id)
    tarefa_obj = Tarefa(titulo=tarefa.titulo, descricao=tarefa.descricao, prioridade_tarefa_id=tarefa.prioridade_tarefa_id, status_tarefa_id=tarefa.status_tarefa_id, data_criacao=tarefa.data_criacao, ativo=True, nota_id=tarefa.nota_id)
    db.session.add(tarefa_obj)
    db.session.commit()

def put_tarefa(id, titulo, descricao, prioridade_tarefa_id, status_tarefa_id):
    tarefa = get_tarefa_by_id(id)
    tarefa.titulo = titulo
    tarefa.descricao = descricao
    tarefa.prioridade_tarefa_id = prioridade_tarefa_id
    tarefa.status_tarefa_id = status_tarefa_id
    db.session.commit()

def del_tarefa(id):
    tarefa = Tarefa.query.filter_by(id=id).first()
    tarefa.ativo = False
    db.session.commit()
    return tarefa