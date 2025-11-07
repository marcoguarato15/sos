from app import app, jwt
from flask import render_template, request, redirect, url_for, make_response
from app.services import usuario_service
from routes import index
from routes.login import login
# @app.route("/")
# def index():
#     return render_template('base.html')


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
