from app import db
from app.models.custom_field_model import CustomField

def get_custom_field():
    custom_field = CustomField.query.all()
    return custom_field

def add_custom_field(custom_field):
    custom_field_obj = CustomField(nome=custom_field.nome, id_custom_field=custom_field.id_custom_field)
    db.session.add(custom_field_obj)
    db.session.commmit()

def put_custom_field(id, nome, id_custom_field):
    custom_field = CustomField.query.filter_by(id=id).first()
    custom_field.nome = nome
    custom_field.id_custom_field = id_custom_field
    db.session.commit()
