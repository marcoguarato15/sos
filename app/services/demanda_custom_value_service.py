from app import db
from app.models.demanda_custom_value_model import DemandaCustomValue

def get_demanda_custom_value():
    demanda_custom_value = DemandaCustomValue.query.all()
    return demanda_custom_value

def add_demanda_custom_value(demanda_custom_value):
    demanda_custom_value_obj = DemandaCustomValue(valor=demanda_custom_value.valor, demanda_id=demanda_custom_value.demanda_id, custom_field_id=demanda_custom_value.custom_field_id)
    db.session.add(demanda_custom_value_obj)
    db.session.commit()

def put_demanda_custom_value(id, valor):
    demanda_custom_value = DemandaCustomValue.query.filter_by(id).first()
    demanda_custom_value.valor = valor
    db.session.commit()

def del_demanda_custom_value(id):
    DemandaCustomValue.query.filter_by(id=id).delete()
    db.session.commit()

def get_demanda_custom_value_by_demanda_id_and_id_custom_field(demanda_id,custom_field_id):
    demanda_custom_value = DemandaCustomValue.query.filter_by(demanda_id=demanda_id, custom_field_id=custom_field_id).first()
    return demanda_custom_value