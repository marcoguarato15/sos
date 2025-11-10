from app import db
from ..models.setor_model import Setor

def get_setores():
    setores = Setor.query.all()
    return setores