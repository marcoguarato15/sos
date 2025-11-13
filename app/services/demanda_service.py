from app import db, app
from app.models.demanda_model import Demanda
import requests

def add_new_demandas():
    api_key = app.config["DEMANDAS_API_KEY"]
    ## URL para todas solicitações
    url = f"https://demandas.uftm.edu.br/projects/projetos-de-redes-digitais/issues.json?key={api_key}&include=custom_fields&limit=100"

    res = requests.get(url).json()
    issues = res["issues"]
    projeto_rede_digital = []
    infraestrutura_rede = []
    servico_rede = []
    demandas_atuais = get_demandas()
    for demanda in issues:
        if demanda["id"] not in demandas_atuais:
            print(demanda["id"])
        else:
            print(f"demanda {demanda["id"]} ja incluida")

    pass

def get_demandas():
    demandas = Demanda.query.all()
    return demandas