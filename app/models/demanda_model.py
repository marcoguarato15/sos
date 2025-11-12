from app import db

class Demanda(db.Model):
    __tablename__ = "demanda"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_demanda = db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    data_inicio = db.Column(db.DateTime, nullable=True)
    data_criacao = db.Column(db.DateTime, nullable=False)
    data_atualizacao = db.Column(db.DateTime, nullable=True)
    data_finalizacao = db.Column(db.DateTime, nullable=True)
    porcentagem_feita = db.Column(db.Integer, nullable=False)

    author_id = db.Column(db.ForeignKey("usuario.id"))
    author = db.relationship("Usuario", backref=db.backref("demanda_criada", lazy="joined"))

    atribuido_para_id = db.Column(db.ForeignKey("usuario.id"))
    atribuido_para = db.relationship("Usuario", backref=db.backref("demanda_atribuida", lazy="joined"))

    status_id = db.Column(db.ForeignKey("status.id"))
    status = db.relationship("Status", backref=db.backref("demanda"), foreign_keys=[status_id])

    titulo_projeto_id = db.Column(db.ForeignKey("titulo_projeto.id"))
    titulo_projeto = db.relationship("TituloProjeto", backref=db.backref("demanda"), foreign_keys=[titulo_projeto_id])

    tipo_id = db.Column(db.ForeignKey("tipo.id"))
    tipo = db.relationship("Tipo", backref=db.backref("demanda"), foreign_keys=[tipo_id])

    prioridade_id = db.Column(db.ForeignKey("prioridade.id"))
    prioridade = db.relationship("Prioridade", backref=db.backref("demanda"), foreign_keys=[prioridade_id])

    categoria_id = db.Column(db.ForeignKey("categoria.id"))
    categoria = db.relationship("Categoria", backref=db.backref("demanda"), foreign_keys=[categoria_id])
