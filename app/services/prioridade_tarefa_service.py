from app.models.prioridade_tarefa_model import PrioridadeTarefa

def get_prioridades_tarefas():
    prioridades_tarefas = PrioridadeTarefa.query.all()
    return prioridades_tarefas

