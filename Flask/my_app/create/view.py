import json
from my_app import app, db
from flask import Blueprint, request, render_template, jsonify
from flask.views import MethodView
from my_app.create.models import Card

create = Blueprint('create', __name__)

@create.route('/teste')
def test():
    return render_template('solicitar.html')

@create.route('/teste', methods=['POST'])
def testando():
    if request.method == 'POST':
        name = request.form['name']
        return name

class CreateView(MethodView):
    def post(self, name, year, cpf, income):
        people = Card(name, year, cpf, income)
        db.session.add(people)
        db.session.commit()
        return jsonify({people.id:{
            'name' : people.name,
            'year' : people.year,
            'cpf' : people.cpf,
            'income' : people.income,
            'score' : people.score,
            'status' : people.status,
        }})

