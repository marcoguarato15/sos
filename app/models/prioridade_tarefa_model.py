from app import db

class PrioridadeTarefa(db.Model):
    __tablename__ = "prioridade_tarefa"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    num_prioridade = db.Column(db.Integer, nullable=False)
