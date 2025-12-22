from app import db
from app.models.tarefa_model import Tarefa
from app.models.status_tarefa_model import StatusTarefa
from datetime import timedelta, time

def get_tarefas(titulo, status_id, prioridade_id):
    query = Tarefa.query

    if titulo:
        query = query.filter(Tarefa.titulo.like(f"%{titulo}%"))
    if status_id:
        query = query.filter(Tarefa.status_tarefa_id == status_id)
    if prioridade_id:
        query = query.filter(Tarefa.prioridade_tarefa_id == prioridade_id)

    tarefas = query.filter((Tarefa.status_tarefa_id != 16) & (Tarefa.status_tarefa.has(StatusTarefa.nome != "Concluida")) & (Tarefa.ativo == True)).all()

    return tarefas

def get_tarefas_indeferidas():
    tarefas_indeferidas = Tarefa.query.filter(Tarefa.status_tarefa.has(StatusTarefa.nome == "Concluida") | Tarefa.status_tarefa.has(StatusTarefa.nome == "Indeferida")).all()
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

def verificar_tempo_total(id):
    tarefa = get_tarefa_by_id(id)
    total = 0
    for atividade in tarefa.atividades:
        duracao = atividade.tempo_estimado
        total += duracao

    tarefa.tempo_gasto_total = total
    db.session.commit()