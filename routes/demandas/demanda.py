from app import app
from flask import render_template, redirect, url_for, flash
from app.decorators.jwt_decorator import jwt_refresh
from app.services import demanda_service

@app.route('/demandas')
@jwt_refresh
def demandas():
    demandas = demanda_service.get_demandas()
    return render_template('demanda/index.html', demandas=demandas)

@app.route('/get/demandas')
@jwt_refresh
def get_demandas():
    try:
        demanda_service.add_new_demandas_from_sos()
        flash("Demandas adicionadas com sucesso","success")
    except Exception as e:
        flash(f"Servidor SOS fora de serviço, {e}","error")
    return redirect(url_for('demandas'))

@app.route("/put_demandas")
@jwt_refresh
def put_demandas():
    demanda_service.put_demandas_from_sos()
    return redirect(url_for('demandas'))
