from app import app
import requests, json
from app.decorators.jwt_decorator import jwt_refresh

@app.route('/get/demandas')
@jwt_refresh
def demandas():
    api_key = app.config["DEMANDAS_API_KEY"]
    url = f"https://demandas.uftm.edu.br/projects/projetos-de-redes-digitais/issues.json?key={api_key}&include-custom_fields&limit=1"
    res = requests.get(url).json()
    print(res["issues"])
    for i in res["issues"]:
        # id da demanda
        print(i["id"])
        # Setor do demandas (desnecessário)
        print(i["project"]["name"])
        #categoria (nullable=False)
        print(i["tracker"]["name"])
        # status (nullable=False, default=NOVA)
        print(i["status"]["name"])
        # prioriade (nullable=False)
        print(i["priority"]["name"])
        # autor/criador (nullable=False)
        print(i["author"]["name"])
        # titulo (nullable=False)
        print(i["subject"])
        # descricao (nullable=True)
        print(i["description"])
        # porcentagem realizada
        print(i["done_ratio"])
        # custom fields (informações da os)
        custom_fields = i["custom_fields"]
        for cf in custom_fields:
            print(cf["id"], cf["name"], cf["value"])


    return "<p>aqui</p>"
