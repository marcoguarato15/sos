from app import db

class Nota(db.Model):
    __tablename__ = "nota"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(255), nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    demanda_id = db.Column(db.ForeignKey("demanda.id"), nullable=True)
    demanda = db.relationship("Demanda", backref=db.backref("nota"), foreign_keys=[demanda_id])

    prioridade_id = db.Column(db.ForeignKey("prioridade.id"), nullable=False)
    prioridade = db.relationship("Prioridade", backref=db.backref("nota", lazy="joined"), foreign_keys=[prioridade_id])