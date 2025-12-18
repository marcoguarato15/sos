from app.models.categoria_atividade_model import CategoriaAtividade

def get_categorias_atividades():
    categorias_atividades = CategoriaAtividade.query.all()
    return categorias_atividades

