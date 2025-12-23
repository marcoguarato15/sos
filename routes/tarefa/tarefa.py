from app import app
from app.services import prioridade_tarefa_service, tarefa_service, nota_service, status_tarefa_service
from app.entidades.tarefa import Tarefa
from flask import render_template, url_for, redirect, flash, request
from flask_jwt_extended import get_jwt, get_jwt_identity
from app.decorators.jwt_decorator import jwt_refresh

@app.route('/tarefas')
@jwt_refresh
def tarefas():
    prioridades = prioridade_tarefa_service.get_prioridades_tarefas()
    status = status_tarefa_service.get_status_tarefas()
    if request.method == "GET":
        titulo = request.args.get("titulo") if request.args.get("titulo") else ""
        status_id = request.args.get("status_id") if request.args.get("status_id") else ""
        prioridade_id = request.args.get("prioridade_id") if request.args.get("prioridade_id") else ""
    tarefas = tarefa_service.get_tarefas(titulo,status_id,prioridade_id)

    return render_template('tarefa/index.html', tarefas=tarefas, prioridades=prioridades, status=status, titulo=titulo, prioridade_id=prioridade_id, status_id=status_id, filter=True)

@app.route('/tarefas/suspensas')
@jwt_refresh
def tarefas_suspensas():
    tarefas = tarefa_service.get_tarefas_indeferidas()

    return render_template('tarefa/index.html', tarefas=tarefas)

@app.route('/post/tarefa', defaults={'nota_id': None}, methods=["GET","POST"]) 
@app.route('/post/tarefa/<int:nota_id>', methods=["GET","POST"])
@jwt_refresh
def post_tarefa(nota_id):
    notas = nota_service.get_notas()
    prioridades = prioridade_tarefa_service.get_prioridades_tarefas()
    status = status_tarefa_service.get_status_tarefas()
    if request.method == "POST":
        if (titulo := request.form.get("titulo")) and (prioridade_tarefa_id := request.form.get('prioridade_id')) and  (status_tarefa_id := request.form.get('status_id')) and (nota_id := request.form.get('nota_id')):
            descricao = "" if request.form.get("descricao") == None else request.form.get("descricao")
            tarefa = Tarefa(titulo, descricao, prioridade_tarefa_id, status_tarefa_id, nota_id)
            tarefa_service.post_tarefa(tarefa)
            flash("Sucesso ao adicionar Tarefa!","success")
            return redirect(url_for('tarefas'))
    return render_template('tarefa/post_tarefa.html', notas=notas, nota_id=nota_id, prioridades=prioridades, status=status)

@app.route('/put/tarefa/<int:id>', methods=["GET","POST"])
@jwt_refresh
def put_tarefa(id):
    tarefa = tarefa_service.get_tarefa_by_id(id)
    prioridades = prioridade_tarefa_service.get_prioridades_tarefas()
    status = status_tarefa_service.get_status_tarefas()
    if request.method == "POST":
        if (titulo := request.form.get("titulo")) and (prioridade_tarefa_id := request.form.get('prioridade_id')) and  (status_tarefa_id := request.form.get('status_id')):
            descricao = "" if request.form.get("descricao") == None else request.form.get("descricao")
            tarefa_service.put_tarefa(id, titulo, descricao, prioridade_tarefa_id, status_tarefa_id)
            flash("Sucesso ao alterar Tarefa!","success")
            return redirect(url_for('tarefas'))
    return render_template('tarefa/put_tarefa.html', tarefa=tarefa, prioridades=prioridades, status=status)

@app.route('/self/tarefa/<int:id>')
@jwt_refresh
def self_tarefa(id):
    tarefa = tarefa_service.get_tarefa_by_id(id)

    return render_template('tarefa/self.html', tarefa=tarefa, atividades=tarefa.atividades)

@app.route("/reativar/tarefa/<int:id>")
def reativar_tarefa(id):
    tarefa_service.reativar_tarefa(id)
    flash("Tarefa reativada com sucesso","success")
    return redirect(url_for("tarefas_suspensas"))