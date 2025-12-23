from app import app
from flask import request, redirect, url_for, render_template, flash
from app.entidades.atividade import Atividade
from app.decorators.jwt_decorator import jwt_refresh
from flask_jwt_extended import get_jwt_identity
from app.services import categoria_atividade_service, status_tarefa_service, usuario_service, atividade_service
from math import floor
@app.route("/atividades")
@jwt_refresh
def atividades():
    usuario_id = get_jwt_identity()
    usuario = usuario_service.get_usuario_by_id(usuario_id)
    atividades = atividade_service.get_atividades_usuario_order_by_prioridade_ordem_execucao(usuario_id)

    return render_template('atividade/index.html', atividades=atividades, papel=usuario.papel)

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
            try:
                atividade_service.post_atividade(atividade=atividade)
                flash("Atividade adicionada com sucesso","success")
                return redirect(url_for('post_atividade', tarefa_id=tarefa_id))
            except Exception as e:
                flash(f"{e}","error")
                return redirect(url_for('post_atividade', tarefa_id=tarefa_id))


    return render_template('atividade/post_atividade.html', usuarios=usuarios, status_tarefas=status_tarefas, categorias_atividades=categorias_atividades, tarefa_id=tarefa_id, )

@app.route("/put/atividade/<int:id>", methods=["GET","POST"])
@jwt_refresh
def put_atividade(id):
    usuarios = usuario_service.get_usuarios()
    status_tarefas = status_tarefa_service.get_status_tarefas()
    categorias_atividades = categoria_atividade_service.get_categorias_atividades()
    atividade = atividade_service.get_atividade_by_id(id)
    usuarios_ids = [usuario.id for usuario in atividade.usuarios]


    tempo_estimado_formatado = atividade_service.formata_tempo_estimado_para_formato_iso(atividade.tempo_estimado)

    if (titulo := request.form.get("titulo")) and (categoria_atividade_id := request.form.get("categoria_atividade_id")) and (status_tarefa_id := request.form.get("status_tarefa_id")) and (tempo_estimado := request.form.get("tempo_estimado")):
        usuarios = request.form.getlist("usuarios")
        
        try:
            atividade_service.put_atividade(id=id, titulo=titulo, categoria_atividade_id=categoria_atividade_id, status_tarefa_id=status_tarefa_id,tempo_estimado=tempo_estimado, usuarios=usuarios)
            flash("Atividade alterada com sucesso","success")
            return redirect(url_for('put_atividade', id=id))
        except Exception as e:
            flash(f"{e}","error")
            return redirect(url_for('put_atividade', id=id))
            
    return render_template("atividade/put_atividade.html", tempo_estimado=tempo_estimado_formatado,usuarios_ids=usuarios_ids, atividade=atividade, usuarios=usuarios, status_tarefas=status_tarefas,categorias_atividades=categorias_atividades)



