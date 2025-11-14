from app import db
from app.models.demanda_custom_value_model import DemandaCustomValue

def get_demanda_custom_value():
    demanda_custom_values = DemandaCustomValue.query.all()
    return demanda_custom_values

def add_demanda_custom_value(demanda_custom_value):
    demanda_custom_value_obj = DemandaCustomValue(nome=demanda_custom_value.nome, demanda_id=demanda_custom_value.demanda_id, custom_field_id=demanda_custom_value.custom_field_id)
    db.session.add(demanda_custom_value_obj)
    db.session.commit()

def put_demanda_custom_value(id, nome, demanda_id, custom_field_id):
    demanda_custom_value = DemandaCustomValue.query.filter_by(id).first()
    demanda_custom_value.nome = nome
    demanda_custom_value.demanda_id = demanda_id
    demanda_custom_value.custom_field_id = custom_field_id
    db.session.commit()
