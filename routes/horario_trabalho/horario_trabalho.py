from app import app
from flask import render_template, redirect, url_for, request, flash
from flask_jwt_extended import get_jwt_identity
from app.services import horario_trabalho_service, usuario_service
from app.decorators.jwt_decorator import jwt_refresh
from app.entidades.horario_trabalho import Horario_trabalho

@app.route("/horarios_trabalho")
@jwt_refresh
def horarios_trabalho():
    horarios_trabalho = horario_trabalho_service.get_horarios_trabalho()
    
    return render_template("horario_trabalho/index.html", horarios_trabalho=horarios_trabalho)

@app.route("/post/horario_trabalho", methods=["GET","POST"])
@jwt_refresh
def post_horario_trabalho():
    
    if request.method == "POST":
        if (horario_inicio := request.form.get("horario_inicio")) and (horario_fim := request.form.get("horario_fim")) and (tipo_turno := request.form.get("tipo_turno")):
            usuario_id = get_jwt_identity()
            criador = usuario_service.get_usuario_by_id(usuario_id)
            try:
                horario_trabalho = Horario_trabalho(horario_inicio=horario_inicio, horario_fim=horario_fim, tipo_turno=tipo_turno, criador_id=criador.id, ativo=True)
                horario_trabalho_service.post_horario_trabalho(horario_trabalho=horario_trabalho)
                flash("Sucesso ao adicionar Horario de Trabalho","success")
                return redirect(url_for('horarios_trabalho'))
            except Exception:
                flash("Falha ao criar Horario de Trabalho","error")
    
    return render_template("horario_trabalho/post_horario_trabalho.html")

@app.route("/put/horario_trabalho/<int:id>", methods=["GET","POST"])
@jwt_refresh
def put_horario_trabalho(id):
    horario_trabalho = horario_trabalho_service.get_horario_trabalho_by_id(id)
    if request.method == "POST":
        if (horario_inicio := request.form.get("horario_inicio")) and (horario_fim := request.form.get("horario_fim")) and (tipo_turno := request.form.get("tipo_turno")):
            try:
                horario_trabalho_service.put_horario_trabalho(id=id, horario_inicio=horario_inicio, horario_fim=horario_fim,tipo_turno=tipo_turno)
                flash("Sucesso ao alterar Horario de Trabalho","success")
                return redirect(url_for('horarios_trabalho'))
            except Exception:
                flash("Falha ao alterar Horario de Trabalho","error")
            
    return render_template("horario_trabalho/put_horario_trabalho.html", horario_trabalho=horario_trabalho)

@app.route("/del/horario_trabalho/<int:id>")
@jwt_refresh
def del_horario_trabalho(id):
    try:
        horario_trabalho_service.del_horario_trabalho(id=id)
        flash("Sucesso ao excluir horário de trabalho","success")
    except Exception:
        flash("Falha ao excluir horário de trabalho","error")

    return redirect(url_for("horarios_trabalho"))