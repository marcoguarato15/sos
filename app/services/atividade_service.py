from app import db
from app.models.atividade_model import Atividade
from app.services import usuario_service, tarefa_service
from datetime import timedelta, time

def get_atividades_da_tarefa(tarefa_id):
    atividades = Atividade.query.filter_by(tarefa_id=tarefa_id).all()
    return atividades

def post_atividade(atividade):

    t = time.fromisoformat(atividade.tempo_estimado)
    tempo_estimado_time = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
    total_segundos = int(tempo_estimado_time.total_seconds())

    ativ = Atividade(titulo=atividade.titulo, tarefa_id=atividade.tarefa_id, tempo_estimado=total_segundos, categoria_atividade_id=atividade.categoria_atividade_id, status_tarefa_id=atividade.status_tarefa_id, data_criacao=atividade.data_criacao)
    for usuario_id in atividade.usuarios:
        usuario = usuario_service.get_usuario_by_id(usuario_id)
        ativ.usuarios.append(usuario)


    db.session.add(ativ)
    db.session.commit()
    tarefa_service.verificar_tempo_total(atividade.tarefa_id)