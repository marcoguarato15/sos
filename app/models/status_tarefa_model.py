from app import db

class StatusTarefa(db.Model):
    __tablename__ = "status_tarefa"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True,nullable=False)
    num_status = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(100), nullable=False)