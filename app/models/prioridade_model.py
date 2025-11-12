from app import db

class Prioridade(db.Model):
    __tablename__ = "prioridade"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    id_prioridade = db.Column(db.Integer, nullable=True)