from app import db
from app.models.status_model import Status


def get_status():
    status = Status.query.all()
    return status

def add_status(status):
    status = Status(id_status=status.id_status, nome=status.nome)

    db.session.add(status)
    db.session.commit()

def put_status(id, id_status, nome):
    status = Status.query.filter_by(id=id).first()
    status.id_status = id_status
    status.nome = nome
    db.session.commit()

def get_status_by_id_status(id_status):
    status = Status.query.filter_by(id_status=id_status).first()
    return status