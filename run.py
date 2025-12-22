from app import app, jwt
from flask import render_template, request, redirect, url_for, make_response
from app.services import usuario_service

from routes import index
from routes.login import login
from routes.usuario import usuario
from routes.demandas import demanda
from routes.nota import nota
from routes.horario_trabalho import horario_trabalho
from routes.setor import setor
from routes.tarefa import tarefa
from routes.atividade import atividade

@jwt.additional_claims_loader
def add_claims_to_access_token(identity):
    usuario = usuario_service.get_usuario_by_id(identity)
    if usuario.papel == "admin":
        papel = "admin"
    else:
        papel = "user"

    return {"papel":papel}


@app.route('/copyright')
def copyright():
    return render_template("copyright.html")
