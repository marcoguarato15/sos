from app import db
from ..models.horario_trabalho_model import HorarioTrabalho

def get_horarios_trabalho():
    horarios_trabalho = HorarioTrabalho.query.all()
    return horarios_trabalho