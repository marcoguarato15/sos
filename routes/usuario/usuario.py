from run import app
from flask import request, redirect, url_for, flash, render_template, make_response
from flask_jwt_extended import get_jwt_identity, get_jwt, set_access_cookies, create_access_token
from app.services import usuario_service, setor_service, horario_trabalho_service
from app.entidades.usuario import Usuario
from app.decorators.jwt_decorator import jwt_refresh
from datetime import timedelta

@app.route("/usuarios")
@jwt_refresh
def usuarios():
    usuarios = usuario_service.get_usuarios()
    for u in usuarios:
        for j in usuarios:
            if u.id == j.criador_id:
                j.criador = u.nome
        
    return render_template("usuario/index.html", usuarios=usuarios)

@app.route('/post/usuario', methods=["GET","POST"])
@jwt_refresh
def post_usuario():
    claims = get_jwt()
    if claims["papel"] == "admin":
        criador_id = get_jwt_identity()
        horarios_trabalho = horario_trabalho_service.get_horarios_trabalho()
        setores = setor_service.get_setores()
        if request.method == "POST":
            if (nome := request.form.get('nome')) and (email := request.form.get('email')) and (disponivel := request.form.get('disponivel')) and (papel := request.form.get('papel')) and (setor_id := request.form.get('setor_id')) and (horario_trabalho_id := request.form.get('horario_trabalho_id')):
                cargo = request.form.get('cargo')
                disponivel =  True if disponivel == 1 else False
                contato = request.form.get('contato')
                print(nome, email, disponivel, papel, setor_id, cargo, contato, horario_trabalho_id)
                usuario_service.add_usuario(Usuario(nome=nome, email=email,senha="123456", cargo=cargo ,setor_id=setor_id, ativo=True, papel=papel, disponivel=disponivel, contato=contato, criador_id=int(criador_id),horario_trabalho_id=horario_trabalho_id))
                flash("Cadastrado com sucesso","success")
                return redirect(url_for('usuarios'))

    else:
        flash("Usuario sem permissão","error")
        return redirect(url_for("index"))

    return render_template('usuario/post_usuario.html', setores=setores, horarios_trabalho=horarios_trabalho)

@app.route('/put/usuario/<int:id>', methods=["GET","POST"])
@jwt_refresh
def put_usuario(id):
    claims = get_jwt()
    if claims["papel"] == "admin":
        usuario = usuario_service.get_usuario_by_id(id)
        horarios_trabalho = horario_trabalho_service.get_horarios_trabalho()
        setores = setor_service.get_setores()
        if request.method == "POST":
            if (nome := request.form.get('nome')) and (email := request.form.get('email')) and (disponivel := request.form.get('disponivel')) and (papel := request.form.get('papel')) and (setor_id := request.form.get('setor_id')) and (horario_trabalho_id := request.form.get('horario_trabalho_id')):
                cargo = request.form.get('cargo')
                disponivel =  True if disponivel == "1" else False
                contato = request.form.get('contato')
                id_demanda = 0 if request.form.get('id_demanda').strip() == '' else int(request.form.get('id_demanda'))
                usuario = usuario_service.put_usuario(id_demanda=id_demanda,nome=nome, email=email, cargo=cargo,setor_id=setor_id, papel=papel, disponivel=disponivel, contato=contato, horario_trabalho_id=horario_trabalho_id, id=id)
                flash("Alteração feita com sucesso","success")

            else:
                flash("Preencha os campos", "error")

    else:
        flash("Usuario sem permissão", "error")
        return redirect(url_for("index"))
    return render_template("usuario/put_usuario.html", usuario=usuario, setores=setores, horarios_trabalho=horarios_trabalho)

@app.route('/del/usuario/<int:id>')
@jwt_refresh
def del_usuario(id):
    claims = get_jwt()
    if claims["papel"] == "admin":
        usuario_service.del_usuario(id)
        flash("Sucesso em deletar usuario","success")
        return redirect(url_for('usuarios'))
    else:
        flash("Usuario sem permissão","error")
        return redirect(url_for('index'))
    
@app.route('/set/senha', methods=["GET", "POST"])
@jwt_refresh
def set_senha():
    if request.method == "POST":
        if (senha := request.form.get('nova-senha')) and (senha2 := request.form.get('nova-senha-2')):
            if senha == senha2:
                identity = get_jwt_identity()
                usuario = usuario_service.get_usuario_by_id(identity)
                usuario_service.set_senha(usuario, senha)
                access_token = create_access_token(
                    identity=str(usuario.id),
                    expires_delta=timedelta(minutes=1),
                    additional_claims={"alter":"False"}
                )
                response = redirect(url_for('index'))
                set_access_cookies(response, access_token)
                flash("Senha alterada com sucesso","success")
                return response
            else:
                flash("Senhas diferentes","error")
        else:
            flash("Preencha os campos","error")
    return render_template('usuario/set_senha.html', senha=senha)