from app import db

class Setor(db.Model):
    __tablename__ = "setor"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    gestor_id = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    gestor = db.relationship("Usuario", foreign_keys=[gestor_id], backref=db.backref("setor_gestorado"))
    
    membros = db.relationship("Usuario", back_populates="setor", foreign_keys="[Usuario.setor_id]")
    data_criacao = db.Column(db.DateTime, nullable=False)
    ultima_atualizacao = db.Column(db.DateTime, nullable=True)

