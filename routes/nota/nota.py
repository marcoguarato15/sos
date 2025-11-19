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
    demandas = demanda_service.get_demandas()
    titulo = None
    demanda = None
    prioridade = None
    if request.method == "POST":
        if (titulo := request.form.get("titulo")) and (demanda := request.form.get("demanda")) and (prioridade := request.form.get("prioridade")):
            nota = Nota(titulo=titulo, demanda_id=demanda, prioridade_id=prioridade)
            # try:
            nota_service.post_nota(nota)
            flash("Sucesso ao adicionar nota","success")
                # return redirect(url_for('notas'))
            # except Exception as e:
            #     flash("Erro ao adicionar nota","error")
            #     return redirect(url_for('post_nota', tit=titulo, pri=prioridade, dem=demanda))
        else:
            flash("Preencha os campos","error")

    return render_template("nota/post_nota.html", demandas=demandas, prioridades=prioridades, tit=titulo, dem=demanda, prio=prioridade)