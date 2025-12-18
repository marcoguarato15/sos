from app import app
from app.services import prioridade_tarefa_service, tarefa_service, nota_service, status_tarefa_service
from app.entidades.tarefa import Tarefa
from flask import render_template, url_for, redirect, flash, request
from flask_jwt_extended import get_jwt, get_jwt_identity
from app.decorators.jwt_decorator import jwt_refresh

@app.route('/tarefas')
@jwt_refresh
def tarefas():
    tarefas = tarefa_service.get_tarefas()

    return render_template('tarefa/index.html', tarefas=tarefas)

@app.route('/post/tarefa', defaults={'nota_id': None}, methods=["GET","POST"]) 
@app.route('/post/tarefa/<int:nota_id>', methods=["GET","POST"])
@jwt_refresh
def post_tarefa(nota_id):
    notas = nota_service.get_notas()
    prioridades = prioridade_tarefa_service.get_prioridades_tarefas()
    status = status_tarefa_service.get_status_tarefas()
    if request.method == "POST":
        pass

    return render_template('tarefa/post_tarefa.html', notas=notas, nota_id=nota_id, prioridades=prioridades, status=status)