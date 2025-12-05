from app import db

class StatusTarefa(db.Model):
    __tablename__ = "status_tarefa"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,nullable=False)
    em_andamento = db.Column(db.Boolean, nullable=False)
    nome = db.Column(db.String(100), nullable=False)