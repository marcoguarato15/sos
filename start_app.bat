@echo off
REM Ativa o ambiente virtual
call C:\Users\Usuario\Documents\estudos\sos\.venv\Scripts\activate

REM Inicia o servidor usando --setup-path para garantir que o diretório seja adicionado ao sys.path
mod_wsgi-express start-server --port 5000 flask_app.wsgi

pause