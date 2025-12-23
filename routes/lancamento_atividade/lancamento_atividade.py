from app import app
from flask import render_template, flash, url_for, redirect, request
from flask_jwt_extended import get_jwt_identity
from app.entidades.lancamento_atividade import LancamentoAtividade
from app.decorators.jwt_decorator import jwt_refresh
from app.services import atividade_service, lancamento_atividade_service, usuario_service

@app.route('/post/lancamento/atividade/<int:atividade_id>', methods=["GET","POST"])
@jwt_refresh
def post_lancamento_atividade(atividade_id):
    atividade = atividade_service.get_atividade_by_id(atividade_id)
    usuario_id = get_jwt_identity()
    usuario = usuario_service.get_usuario_by_id(usuario_id)
    usuarios = atividade.usuarios
    if request.method == "POST":
        if (tempo_gasto := request.form.get('tempo_gasto')) and (usuario_id := request.form.get('usuario_id')):
            descricao = request.form.get('descricao')

            lancamento = LancamentoAtividade(usuario_id=usuario_id, atividade_id=atividade_id, descricao=descricao, tempo_gasto=tempo_gasto)

            lancamento_atividade_service.post_lancamento_atividade(lancamento)
            flash("Sucesso ao lançar atividade","success")

    return render_template('lancamento_atividade/post_lancamento_atividade.html', atividade=atividade, usuarios=usuarios, usuario_id=usuario.id, papel=usuario.papel)