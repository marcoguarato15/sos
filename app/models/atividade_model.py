from app import db

atividade_usuario = db.Table("atividade_usuario", 
db.Column("usuario_id", db.Integer, db.ForeignKey("usuario.id"), primary_key=True, nullable=False),
db.Column("atividade_id", db.Integer, db.ForeignKey("atividade.id"), primary_key=True, nullable=False))

class Atividade(db.Model):
    __tablename__ = "atividade"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    titulo = db.Column(db.Text, nullable=True)
    tempo_estimado = db.Column(db.Integer, nullable=False)
    tempo_gasto = db.Column(db.Integer, nullable=True)
    data_criacao = db.Column(db.DateTime, nullable=False)
    data_conclusao = db.Column(db.DateTime, nullable=True)

    tarefa_id = db.Column(db.ForeignKey("tarefa.id"))
    tarefa = db.relationship("Tarefa", backref=db.backref("atividades", lazy="joined"), foreign_keys=[tarefa_id])
    
    categoria_atividade_id = db.Column(db.ForeignKey("categoria_atividade.id"))
    categoria_atividade = db.relationship("CategoriaAtividade", backref=db.backref("atividade"), foreign_keys=[categoria_atividade_id])

    status_tarefa_id = db.Column(db.ForeignKey("status_tarefa.id"))
    status_tarefa = db.relationship("StatusTarefa", backref=db.backref("atividade", lazy="joined"), foreign_keys=[status_tarefa_id])

    usuarios = db.relationship("Usuario", secondary="atividade_usuario", back_populates="atividades")