from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
import os

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir, )

app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


from .models import usuario_model, horario_trabalho_model, setor_model, status_model, titulo_projeto_model, tipo_model, demanda_model, custom_field_model, demanda_custom_value_model, categoria_model, prioridade_model