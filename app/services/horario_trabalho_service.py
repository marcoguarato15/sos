from app import db
from ..models.horario_trabalho_model import HorarioTrabalho
from datetime import datetime

def get_horarios_trabalho():
    horarios_trabalho = HorarioTrabalho.query.filter_by(ativo=True).all()
    return horarios_trabalho

def get_horario_trabalho_by_id(id):
    horario_trabalho = HorarioTrabalho.query.filter_by(id=id).first()
    return horario_trabalho

def post_horario_trabalho(horario_trabalho):
    ht = HorarioTrabalho(horario_inicio=horario_trabalho.horario_inicio, horario_fim=horario_trabalho.horario_fim, tipo_turno=horario_trabalho.tipo_turno, data_criacao=horario_trabalho.data_criacao, criador_id=horario_trabalho.criador_id, ativo=horario_trabalho.ativo)
    db.session.add(ht)
    db.session.commit()

def put_horario_trabalho(id, horario_inicio, horario_fim, tipo_turno):
    horario_trabalho = get_horario_trabalho_by_id(id)
    horario_trabalho.horario_inicio = horario_inicio
    horario_trabalho.horario_fim = horario_fim
    horario_trabalho.tipo_turno = tipo_turno
    horario_trabalho.data_atualizacao = datetime.now()
    db.session.commit()

def del_horario_trabalho(id):
    horario_trabalho = get_horario_trabalho_by_id(id)
    horario_trabalho.ativo = False
    horario_trabalho.data_atualizacao = datetime.now()
    db.session.commit()
