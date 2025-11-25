from flask import render_template, redirect, url_for, request, flash
from app.services import nota_service, prioridade_service, demanda_service
from app import app
from app.decorators.jwt_decorator import jwt_refresh
from app.entidades.nota import Nota

@app.route("/notas")
@jwt_refresh
def notas():
    notas = nota_service.get_notas()

    return render_template('nota/index.html', notas=notas)

@app.route("/post/nota", methods=["GET","POST"])
def post_nota():
    prioridades = prioridade_service.get_prioridades()
    demandas = demanda_service.get_demandas_ativas()
    titulo = None
    demanda = None
    prioridade = None
    if request.method == "POST":
        if (titulo := request.form.get("titulo")) and (demanda := request.form.get("demanda")) and (prioridade := request.form.get("prioridade")):
            nota = Nota(titulo=titulo, demanda_id=demanda, prioridade_id=prioridade, ativo=True)
            try:
                nota_service.post_nota(nota)
                flash("Sucesso ao adicionar nota","success")
                return redirect(url_for('notas'))
            except Exception as e:
                flash("Erro ao adicionar nota","error")
                return redirect(url_for('post_nota', tit=titulo, pri=prioridade, dem=demanda))

    return render_template("nota/post_nota.html", demandas=demandas, prioridades=prioridades, tit=titulo, dem=demanda, prio=prioridade)

@app.route("/put/nota/<int:id>", methods=["GET", "POST"])
@jwt_refresh
def put_nota(id):
    nota = nota_service.get_nota_by_id(id)
    demandas = demanda_service.get_demandas_ativas()
    prioridades = prioridade_service.get_prioridades()
    if request.method == "POST":
        print(request.form.get("prioridade_id"))
        print(request.form.get("demanda_id"))
        print(request.form.get("titulo"))
        if (titulo := request.form.get('titulo')) and (demanda_id := request.form.get('demanda_id')) and (prioridade_id := request.form.get('prioridade_id')):
            try:
                nota_service.put_nota(id, titulo, demanda_id, prioridade_id)
                flash("Sucesso ao alterar Nota","success")
                return redirect(url_for('notas'))
            except Exception:
                flash("Falha ao alterar Nota","error")

    return render_template("nota/put_nota.html", demandas=demandas, prioridades=prioridades, nota=nota)

@app.route("/del/nota/<int:id>")
@jwt_refresh
def del_nota(id):
    try:
        nota_service.del_nota(id=id)
        flash("Nota excluida com sucesso","success")
    except Exception:
        flash("Falha ao excluir nota","error")

    return redirect(url_for('notas'))