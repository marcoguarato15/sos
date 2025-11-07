from run import app
from app import jwt
from flask import request, make_response, redirect, url_for, flash, render_template
from app.services import usuario_service
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
from datetime import timedelta

@jwt.additional_claims_loader
def add_claims_to_access_token(identity):
    usuario = usuario_service.get_usuario_by_id(identity)
    if usuario.papel == "admin":
        papel = "admin"
    else:
        papel = "user"

    return {"papel":papel}

@app.route('/login', methods=["GET", "POST"])
def login():
    email = None
    if request.method == "POST":
        if (email := request.form.get("email").strip()) and (senha := request.form.get("senha").strip()):
            usuario = usuario_service.get_usuario_by_email(email)
            if usuario and usuario.decriptar_senha(senha):
                print("ERROR: ",vars(usuario))
                access_token = create_access_token(
                    identity=str(usuario.id),
                    expires_delta=timedelta(minutes=10)
                )
                refresh_token = create_refresh_token(
                    identity=str(usuario.id),
                    expires_delta=timedelta(minutes=15)
                )
                response = make_response(redirect(url_for("index")))
                set_access_cookies(response, access_token)
                set_refresh_cookies(response, refresh_token)
                return response
            else:
                flash("Credenciais inválidas", "error")

    return render_template("login/index.html",email=email)