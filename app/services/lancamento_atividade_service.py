from app import db
from app.models.lancamento_atividade_model import LancamentoAtividade
from app.services import atividade_service
from app.helpers.helpers import formata_tempo_estimado_para_segundos, formata_tempo_estimado_para_formato_iso

def post_lancamento_atividade(lancamento):
    tempo_gasto = formata_tempo_estimado_para_segundos(lancamento.tempo_gasto)

    lancamento = LancamentoAtividade(usuario_id=lancamento.usuario_id, atividade_id=lancamento.atividade_id, descricao=lancamento.descricao, data_criacao=lancamento.data_criacao, tempo_gasto=tempo_gasto)
    db.session.add(lancamento)
    db.session.commit()
    atividade_service.verificar_tempo_gasto(lancamento.atividade_id)

