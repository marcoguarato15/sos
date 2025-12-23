from app import db

class LancamentoAtividade(db.Model):
    __tablename__ = "lancamento_atividade"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    usuario_id = db.Column(db.ForeignKey("usuario.id"))
    usuario = db.relationship("Usuario", backref=db.backref("lancamentos"), foreign_keys=[usuario_id])

    atividade_id = db.Column(db.ForeignKey("atividade.id"))
    atividade = db.relationship("Atividade", backref=db.backref("lancamentos"), foreign_keys=[atividade_id])

    tempo_gasto = db.Column(db.Integer, nullable=False)

    descricao = db.Column(db.String(255), nullable=True)

    data_criacao = db.Column(db.DateTime, nullable=False)