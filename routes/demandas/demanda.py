from app import app
import requests
from flask import render_template, redirect, url_for
from app.decorators.jwt_decorator import jwt_refresh
from app.services import demanda_service

@app.route('/get/demandas')
def get_demandas():
    demandas = demanda_service.add_new_demandas()
    return redirect(url_for(demandas))
    ## URL para todas solicitações


@app.route('/demandas')
@jwt_refresh
def demandas():
    demandas = demanda_service.get_demandas()

    return render_template('demanda/index.html', demandas=demandas)
