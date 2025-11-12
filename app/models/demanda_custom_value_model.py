from app import db

class DemandaCustomValue(db.Model):
    __tablename__ = "demanda_custom_value"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)

    # relacionamentos
    demanda_id = db.Column(db.ForeignKey("demanda.id"))
    demanda = db.relationship("Demanda", backref=db.backref("custom_value", lazy="joined"), foreign_keys=[demanda_id] )

    custom_field_id = db.Column(db.ForeignKey("custom_field.id"))
    custom_field = db.relationship("CustomField", backref=db.backref("custom_value", lazy="joined"), foreign_keys=[custom_field_id])