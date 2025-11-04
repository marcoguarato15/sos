from app import app
from flask import render_template, request, redirect, url_for, make_response

from routes import index

# @app.route("/")
# def index():
#     return render_template('base.html')