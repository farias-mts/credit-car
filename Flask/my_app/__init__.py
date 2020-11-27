from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

file_path = os.path.abspath(os.getcwd())+"/database.db"
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
db = SQLAlchemy(app)

from my_app.generate.views import generate
app.register_blueprint(generate)

from my_app.create.view import create
app.register_blueprint(create)

db.create_all()