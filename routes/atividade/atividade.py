from app import app
from flask import request, redirect, url_for, render_template, flash
from app.entidades.atividade import Atividade
from app.decorators.jwt_decorator import jwt_refresh
from app.services import categoria_atividade_service, status_tarefa_service, usuario_service, atividade_service

@app.route("/post/atividade/<int:tarefa_id>", methods=["GET", "POST"])
@jwt_refresh
def post_atividade(tarefa_id):
    usuarios = usuario_service.get_usuarios()
    status_tarefas = status_tarefa_service.get_status_tarefas()
    categorias_atividades = categoria_atividade_service.get_categorias_atividades()
    if request.method == "POST":
        if (titulo := request.form.get("titulo")) and (categoria_atividade_id := request.form.get("categoria_atividade_id")) and (status_tarefa_id := request.form.get("status_tarefa_id")) and (tempo_estimado := request.form.get("tempo_estimado")):
            usuarios = request.form.getlist("usuarios")
            atividade = Atividade(titulo=titulo, tarefa_id=tarefa_id, tempo_estimado=tempo_estimado,categoria_atividade_id=categoria_atividade_id,status_tarefa_id=status_tarefa_id,usuarios=usuarios)
            atividade_service.post_atividade(atividade=atividade)
            flash("Atividade adicionada com sucesso","success")
            return redirect(url_for('post_atividade', tarefa_id=tarefa_id))

    
    return render_template('atividade/post_atividade.html', usuarios=usuarios, status_tarefas=status_tarefas, categorias_atividades=categorias_atividades, tarefa_id=tarefa_id)

