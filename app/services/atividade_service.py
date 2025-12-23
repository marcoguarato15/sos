from app import db
from app.models.atividade_model import Atividade
from app.models.usuario_model import Usuario
from app.models.tarefa_model import Tarefa
from app.models.prioridade_tarefa_model import PrioridadeTarefa
from app.models.categoria_atividade_model import CategoriaAtividade
from app.models.status_tarefa_model import StatusTarefa
from app.services import usuario_service, tarefa_service
from datetime import timedelta, time
from math import floor
from app.helpers.helpers import formata_tempo_estimado_para_formato_iso, formata_tempo_estimado_para_segundos
class TempoLimiteUltrapassado(Exception):
    def __init__(self, nome):
        self.message = f"Tempo limite semanal de 40 horas de atividade ultrapassado para {nome}"
        super().__init__(self.message)

def get_atividades_da_tarefa(tarefa_id):
    atividades = Atividade.query.filter_by(tarefa_id=tarefa_id).all()
    return atividades

def post_atividade(atividade):

    total_segundos = formata_tempo_estimado_para_segundos(atividade.tempo_estimado)
    ativ = Atividade(titulo=atividade.titulo, tarefa_id=atividade.tarefa_id, tempo_estimado=total_segundos, categoria_atividade_id=atividade.categoria_atividade_id, status_tarefa_id=atividade.status_tarefa_id, data_criacao=atividade.data_criacao)
    for usuario_id in atividade.usuarios:
        usuario = usuario_service.get_usuario_by_id(usuario_id)
        atividades_semanais = usuario.atividades
        horas_semanais = 0
        if int(atividade.status_tarefa_id) == 10:
             for atividade in atividades_semanais:
                if atividade.status_tarefa_id == 10:
                    horas_semanais += atividade.tempo_estimado
        if ( horas_semanais + total_segundos) > 144000:
            possibilidade_tempo = 144000 - horas_semanais
            raise TempoLimiteUltrapassado(f"{usuario.nome}, Tempo possível: {formata_tempo_estimado_para_formato_iso(possibilidade_tempo)}")
        
        if usuario not in atividade.usuarios:
            ativ.usuarios.append(usuario)


    db.session.add(ativ)
    db.session.commit()
    tarefa_service.verificar_tempo_total(atividade.tarefa_id)

def put_atividade(id, titulo, categoria_atividade_id, status_tarefa_id,tempo_estimado, usuarios):
    atividade = get_atividade_by_id(id)
    atividade.titulo = titulo
    atividade.categoria_atividade_id = categoria_atividade_id
    atividade.status_tarefa_id = status_tarefa_id
    atividade.tempo_estimado = formata_tempo_estimado_para_segundos(tempo_estimado)


    for usr in usuarios:
        usuario = usuario_service.get_usuario_by_id(usr)
        atividades_semanais = usuario.atividades
        horas_semanais = 0
        if int(atividade.status_tarefa_id) == 10:
            for atividade_semanal in atividades_semanais:
                if atividade_semanal.status_tarefa_id == 10:
                    horas_semanais += atividade_semanal.tempo_estimado
        
            print(formata_tempo_estimado_para_formato_iso(horas_semanais))
            if (horas_semanais + atividade.tempo_estimado) > 144000:
                possibilidade_tempo = 144000 - horas_semanais
                raise TempoLimiteUltrapassado(f"{usuario.nome}, Tempo possível: {formata_tempo_estimado_para_formato_iso(possibilidade_tempo)}")
        atividade.usuarios.append(usuario)

    for usuario in list(atividade.usuarios):
        if str(usuario.id) not in usuarios:
            atividade.usuarios.remove(usuario)

    if atividade.tarefa.status_tarefa_id != 10:
        atividade.tarefa.status_tarefa_id = 10

    if atividade.tarefa.prioridade_tarefa.num_prioridade == 5:
        atividade.tarefa.prioridade_tarefa_id = 5

    db.session.commit()

def get_atividade_by_id(id):
    atividade = Atividade.query.filter_by(id=id).first()
    return atividade

def get_atividades_usuario_order_by_prioridade_ordem_execucao(usuario_id):
    atividades = Atividade.query.join(Atividade.tarefa).join(Tarefa.status_tarefa).join(Tarefa.prioridade_tarefa).join(Atividade.categoria_atividade).filter(
        StatusTarefa.num_status == 1,
        Atividade.usuarios.any(Usuario.id == usuario_id),
        Atividade.status_tarefa.has(StatusTarefa.num_status == 1),
        Atividade.tarefa.has(Tarefa.prioridade_tarefa_id != 6)
    ).order_by(PrioridadeTarefa.num_prioridade,CategoriaAtividade.ordem_execucao).all()

    return atividades

def verificar_tempo_gasto(atividade_id):
    atividade = get_atividade_by_id(atividade_id)
    tempos_lancados = atividade.lancamentos

    total = 0
    for lancamento in tempos_lancados:
        total += lancamento.tempo_gasto

    atividade.tempo_gasto = total
    db.session.commit()

