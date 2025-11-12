from app import db

class TituloProjeto(db.Model):
    __tablename__ = "titulo_projeto"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_titulo_projeto = db.Column(db.Integer, nullable=True)
    nome = db.Column(db.String(100), nullable=False)

