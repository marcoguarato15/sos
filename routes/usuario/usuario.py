from run import app
from flask import request, redirect, url_for, flash, render_template
from app.services import usuario_service
from app.decorators.jwt_decorator import jwt_refresh

@app.route("/usuarios")
def usuarios():
    usuarios = usuario_service.get_usuarios()
    for u in usuarios:
        usuario = usuario_service.get_usuario_by_id(u.criador_id)
        u.criador = usuario.nome
    return render_template("usuario/index.html", usuarios=usuarios)
