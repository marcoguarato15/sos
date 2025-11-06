from flask import render_template
from run import app
from app.services.usuario_service import get_usuarios

@app.route("/")
def index():
    usuarios = get_usuarios()
    print(usuarios)
    for u in usuarios:
        print(vars(u))
    return render_template("base.html", usuarios=usuarios)
