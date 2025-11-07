from flask import render_template
from run import app
from app.services.usuario_service import get_usuarios
from flask_jwt_extended import get_jwt
from app.decorators.jwt_decorator import jwt_refresh

@app.route("/")
@jwt_refresh
def index():
    claims = get_jwt()
    if claims["papel"] == "admin":
        return render_template("home/adm.html")
    else:
        return render_template("home/index.html")
        
