from app import db

class Tarefa(db.Model):
    __tablename__ = "tarefa"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    ativo = db.Column(db.Boolean, nullable=False)
    prioridade_tarefa_id = db.Column(db.ForeignKey("prioridade_tarefa.id"))
    prioridade_tarefa = db.relationship("PrioridadeTarefa", backref=db.backref("tarefas", lazy="joined"), foreign_keys=[prioridade_tarefa_id])

    status_tarefa_id = db.Column(db.ForeignKey("status_tarefa.id"))
    status_tarefa = db.relationship("StatusTarefa", backref=db.backref("tarefas", lazy="joined"), foreign_keys=[status_tarefa_id])

    tempo_gasto_total = db.Column(db.Time, nullable=True)
    data_criacao = db.Column(db.DateTime, nullable=False)
    data_conclusao = db.Column(db.DateTime, nullable=True)



