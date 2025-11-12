from app import db

class Categoria(db.Model):
    __tablename__ = "categoria"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    id_categoria = db.Column(db.Integer, nullable=True)

    # relacionamento com titulo_projeto
    titulo_projeto_id = db.Column(db.ForeignKey("titulo_projeto.id"))
    titulo_projeto = db.relationship("TituloProjeto", backref=db.backref("categoria_projeto", lazy="joined"), foreign_keys=[titulo_projeto_id])