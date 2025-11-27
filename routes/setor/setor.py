from app import app
from app.decorators.jwt_decorator import jwt_refresh
from flask import render_template, redirect, url_for, flash
from app.services import setor_service, usuario_service

@app.route("/setores")
@jwt_refresh
def setores():
    setores = setor_service.get_setores()
    return render_template('setor/index.html', setores=setores)

