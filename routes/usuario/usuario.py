from run import app
from flask import request, redirect, url_for, flash, render_template
from flask_jwt_extended import get_jwt_identity, get_jwt
from app.services import usuario_service, setor_service, horario_trabalho_service
from app.decorators.jwt_decorator import jwt_refresh

@app.route("/usuarios")
@jwt_refresh
def usuarios():
    usuarios = usuario_service.get_usuarios()
    for u in usuarios:
        for j in usuarios:
            if u.id == j.criador_id:
                j.criador = u.nome
        
    return render_template("usuario/index.html", usuarios=usuarios)

@app.route('/post/usuario', methods=["GET","POST"])
@jwt_refresh
def post_usuario():
    claims = get_jwt()
    if claims["papel"] == "admin":
        criador_id = get_jwt_identity()
        horarios_trabalho = horario_trabalho_service.get_horarios_trabalho()
        setores = setor_service.get_setores()
        if request.method == "post":
            pass
    else:
        flash("Usuario sem permissão","error")
        return redirect(url_for('home/index.html'))

    return render_template('usuario/post_usuario.html', setores=setores, horarios_trabalho=horarios_trabalho)