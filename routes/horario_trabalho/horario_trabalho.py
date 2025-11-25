from app import app
from flask import render_template, redirect, url_for
from app.services import horario_trabalho_service
from app.decorators.jwt_decorator import jwt_refresh

@app.route("/horarios_trabalho")
@jwt_refresh
def horarios_trabalho():
    horarios_trabalho = horario_trabalho_service.get_horarios_trabalho()
    
    return render_template("horario_trabalho/index.html", horarios_trabalho=horarios_trabalho)

@app.route("/post/horario_trabalho", methods=["GET","POST"])
@jwt_refresh
def post_horario_trabalho():
    
    
    
    return render_template("horario_trabalho/post_horario_trabalho.html")