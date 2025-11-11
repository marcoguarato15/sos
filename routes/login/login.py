from run import app
from app import jwt
from flask import request, make_response, redirect, url_for, flash, render_template
from app.services import usuario_service
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
from datetime import timedelta

@app.route('/login', methods=["GET", "POST"])
def login():
    email = None
    if request.method == "POST":
        if (email := request.form.get("email").strip()) and (senha := request.form.get("senha").strip()):
            ## (REGEX) Fazer verificação de regex para depois aceitar valores de busca para o banco

            usuario = usuario_service.get_usuario_by_email(email)
            if(senha == "123456"):
                alter = "True"
            else:
                alter = "False"
            if usuario and usuario.decriptar_senha(senha):
                usuario_service.set_ultimo_login(usuario)
                access_token = create_access_token(
                    identity=str(usuario.id),
                    expires_delta=timedelta(minutes=5),
                    additional_claims={"alter":alter}
                )
                refresh_token = create_refresh_token(
                    identity=str(usuario.id),
                    expires_delta=timedelta(minutes=15),
                )
                response = make_response(redirect(url_for("index")))
                set_access_cookies(response, access_token)
                set_refresh_cookies(response, refresh_token)
                return response
            else:
                flash("Credenciais inválidas", "error")
        else:
            flash("Preencha os campos","error")

    return render_template("login/index.html",email=email)