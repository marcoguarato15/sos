from app import app
from app.decorators.jwt_decorator import jwt_refresh
from flask import render_template, redirect, url_for, flash, request
from app.services import setor_service, usuario_service
from app.entidades.setor import Setor

@app.route("/setores")
@jwt_refresh
def setores():
    setores = setor_service.get_setores()
    return render_template('setor/index.html', setores=setores)

@app.route("/post/setor", methods=["GET","POST"])
@jwt_refresh
def post_setor():
    usuarios = usuario_service.get_usuarios()
    if request.method == "POST":
        if(nome := request.form.get('nome')) and (gestor_id := request.form.get('gestor_id')):
            try:
                setor = Setor(nome=nome, gestor_id=gestor_id, ativo=True)
                setor_service.post_setor(setor)
                flash("Sucesso ao adicionar Setor","success")
                return redirect(url_for('setores'))
            except Exception:
                flash("Falha ao adicionar Setor","error")

    return render_template("setor/post_setor.html", usuarios=usuarios)

@app.route("/put/setor/<int:id>", methods=["GET","POST"])
@jwt_refresh
def put_setor(id):
    setor = setor_service.get_setor_by_id(id)
    usuarios = usuario_service.get_usuarios()
    if request.method == "POST":
        if(nome := request.form.get('nome')) and (gestor_id := request.form.get('gestor_id')):
            try:
                setor_service.put_setor(id,nome,gestor_id)
                flash("Sucesso ao alterar Setor","success")
            except Exception:
                flash("Falha ao alterar Setor","error")
            
    return render_template("setor/put_setor.html", setor=setor, usuarios=usuarios)

@app.route("/del/setor/<int:id>")
@jwt_refresh
def del_setor(id):
    try:
        setor_service.del_setor(id=id)
        flash("Sucesso ao excluir Setor","success")
        return redirect(url_for('setores'))
    except Exception:
        flash("Falha ao excluir Setor","error")
        