from app import db
from passlib.hash import pbkdf2_sha256

class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    setor_id = db.Column(db.Integer, db.ForeignKey("setor.id"))
    setor = db.relationship("Setor", back_populates="membros", foreign_keys=[setor_id])

    ativo = db.Column(db.Boolean, nullable=False)
    papel = db.Column(db.String(50), nullable=False)
    disponivel = db.Column(db.Boolean, nullable=False)
    contato = db.Column(db.String(100), nullable=True)
    criador_id = db.Column(db.Integer, nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False)
    ultima_atualizacao = db.Column(db.DateTime, nullable=True)
    ultimo_login = db.Column(db.DateTime, nullable=True)
    deletado_em = db.Column(db.DateTime, nullable=True)

    horario_trabalho_id = db.Column(db.Integer, db.ForeignKey("horario_trabalho.id"))
    horario_trabalho = db.relationship("HorarioTrabalho", backref=db.backref("horario_atribuido", lazy="joined"), foreign_keys=[horario_trabalho_id])

    def encriptar_senha(self):
        self.senha = pbkdf2_sha256.using(rounds=600000, salt_size=32).hash(self.senha)

    def decriptar_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)