from app.models.status_tarefa_model import StatusTarefa

def get_status_tarefas():
    status_tarefas = StatusTarefa.query.all()
    return status_tarefas

