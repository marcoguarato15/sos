from app import db

class HorarioTrabalho(db.Model):
    __tablename__ = "horario_trabalho"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    horario_inicio = db.Column(db.Time, nullable=False)
    horario_fim = db.Column(db.Time, nullable=False)
    tipo_turno = db.Column(db.String(30), nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False)
    data_atualizacao = db.Column(db.DateTime, nullable=True)
    ativo = db.Column(db.Boolean, nullable=False)

    criador_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    criador = db.relationship("Usuario", backref=db.backref("usuario_criador"), foreign_keys=[criador_id])