from app import db, app
from app.models.demanda_model import Demanda
from app.services import demanda_custom_value_service, titulo_projeto_service, status_service, prioridade_service, tipo_service, categoria_service, custom_field_service, usuario_service
from app.entidades.demanda_custom_value import DemandaCustomValue
import datetime
import requests

def get_demandas():
    demandas = Demanda.query.all()
    return demandas

def add_new_demandas():
    api_key = app.config["DEMANDAS_API_KEY"]
    ## URL para todas solicitações
    url = f"https://demandas.uftm.edu.br/projects/projetos-de-redes-digitais/issues.json?key={api_key}&include=custom_fields&limit=100"

    res = requests.get(url).json()
    issues = res["issues"]
    titulos = titulo_projeto_service.get_titulo_projeto()
    tipos = tipo_service.get_tipo()
    status = status_service.get_status()
    prioridades = prioridade_service.get_prioridade()
    categorias = categoria_service.get_categoria()
    custom_fields = custom_field_service.get_custom_field()
    usuarios = usuario_service.get_usuarios()
    demandas_atuais = get_demandas()
    id_demandas_atuais = [i.id_demanda for i in demandas_atuais]
    for issue in issues:

        id_demanda = None
        titulo_projeto_id = None
        tipo_id = None
        data_criacao = None
        data_estimada = None
        data_inicio = None
        data_atualizacao = None
        prioridade_id = None
        status_id = None
        data_conclusao = None
        atribuido_para = None
        print(issue["id"])
        

        # for demanda in demandas_atuais:
        #     print("id",demanda.id_demanda)
        #     if issue["id"] == demanda.id_demanda:
        #         print(f"Tem essa {issue["id"]}")
        if issue["id"] not in id_demandas_atuais:
            print(issue["id"])
            demanda = {}
            id_demanda = issue["id"]
            if "project" in issue:
                for tp in titulos:
                    if tp.id_titulo_projeto == issue["project"]["id"]:
                        titulo_projeto_id = tp.id
            if "tracker" in issue:
                for t in tipos:
                    if t.id_tipo == issue["tracker"]["id"]:
                        tipo_id = t.id
            if "status" in issue:
                for s in status:
                    if s.id_status == issue["status"]["id"]:
                        status_id = s.id
            if "priority" in issue:
                for p in prioridades:
                    if p.id_prioridade == issue["priority"]["id"]:
                        prioridade_id = p.id
            if "category" in issue:
                for c in categorias:
                    if c.id_categoria == issue["category"]["id"]:
                        categoria_id = c.id
            # alterar verificação ao colocar todos usuários
            if "author" in issue:
                author_id = 1
            if "assigned_to" in issue:
                for u in usuarios:
                    if u.id_usuario == issue["assigned_to"]["id"]:
                        usuario = u.id
            if "subject" in issue:
                titulo = issue["subject"]
            if "description" in issue:
                descricao = issue["description"]
            if "done_ratio" in issue:
                porcentagem_feita = issue["done_ratio"]
            if "created_on" in issue:
                data_criacao = replace_datetime_utc(issue["created_on"])

            if "start_date" in issue:
                data_inicio = issue["start_date"]
            if "due_date" in issue:
                data_estimada = issue["due_date"]
            if "updated_on" in issue:
                data_atualizacao = replace_datetime_utc(issue["updated_on"])
            if "closed_on" in issue:
                data_conclusao = replace_datetime_utc(issue["closed_on"])
            demanda = Demanda(id_demanda=id_demanda, titulo=titulo,categoria_id=categoria_id, status_id=status_id, descricao=descricao, atribuido_para=atribuido_para, data_inicio=data_inicio, data_criacao=data_criacao, data_estimada=data_estimada,prioridade_id=prioridade_id, data_atualizacao=data_atualizacao, titulo_projeto_id=titulo_projeto_id, porcentagem_feita=porcentagem_feita, author_id=author_id, tipo_id=tipo_id,data_conclusao=data_conclusao)

            db.session.add(demanda)
            db.session.commit()
            id_demandas_atuais.append(demanda.id_demanda)

            demanda_db = get_demanda_by_id_demanda(id_demanda)
            id_demanda_db = demanda_db.id

            # passa por todos custom fields
            for cf in issue["custom_fields"]:
                # passa por todas verificações de custom_field_id criadas
                for cf_obj in custom_fields:
                    # verifica se são o mesmo e quando for o mesmo adiciona o valor com o id da demanda corretamente
                    if cf["id"] == cf_obj.id_custom_field:
                        # passa na verificação e verifica se tem valor
                        if "value" in cf and cf["value"] != "":
                            demanda_custom_value = DemandaCustomValue(valor=cf["value"], demanda_id=id_demanda_db, custom_field_id=cf_obj.id)
                            demanda_custom_value_service.add_demanda_custom_value(demanda_custom_value)
            
        else:
                print(f"{issue["id"]} já incluída")

    

def get_demandas():
    demandas = Demanda.query.all()
    return demandas

def get_demanda_by_id_demanda(id_demanda):
    demanda = Demanda.query.filter_by(id_demanda=id_demanda).first()
    return demanda

def replace_datetime_utc(data):
    data_naive = data.replace("T", " ")
    data_naive = data_naive.replace("Z", "")

    return data_naive