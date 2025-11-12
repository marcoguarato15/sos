from app import db

class Status(db.Model):
    __tablename__ = "status"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    id_status = db.Column(db.Integer, nullable=True)