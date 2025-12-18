from app import db

class CategoriaAtividade(db.Model):
    __tablename__ = "categoria_atividade"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    ordem_execucao = db.Column(db.Integer, nullable=False)