from app import db

class CustomField(db.Model):
    __tablename__ = "custom_field"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_custom_field = db.Column(db.Integer, nullable=True)
    nome = db.Column(db.String(100), nullable=False)