import json
from flask import request, jsonify, Blueprint, abort, render_template
from flask.views import MethodView
from my_app import db, app
from my_app.generate.models import Generate

generate = Blueprint('generate', __name__)

@generate.route('/')
def home():
    return render_template('index.html')

@generate.route('/soli.ta/')
def requests():
    return render_template('solicitar.html')

@generate.route('/soli.ta/', methods=['POST'])
def request_post():
    name = request.form['name']
    year = request.form['year']
    cpf = request.form['cpf']
    income = request.form['income']
    return name
    

class GenerateView(MethodView):
    def get(self, id=None, page=1):
        if not id:
            peoples = Generate.query.paginate(page, 10).items
            res={}
            for people in peoples:
                res[people.id]={
                    'name':people.name,
                    'year':people.year,
                    'cpf':people.cpf,
                    'income':people.income,
                    'score':people.score,
                    'status':people.status,
                }
        else:
            people = Generate.query.filter_by(id=id).first()
            if not people:
                abort(404)
            res={
                'name':people.name,
                'year':people.year,
                'cpf':people.cpf,
                'income':people.income,
                'score':people.score,
                'status':people.status,
            }
        return jsonify(res)

    def post(self):
        name = request.form.get('name')
        year = request.form.get('year')
        cpf = request.form.get('cpf')
        income = request.form.get('income')
        print(income)
        people = Generate(name, year, cpf, income)
        db.session.add(people)
        db.session.commit()
        return jsonify({people.id:{
            'name':people.name,
            'year':people.year,
            'cpf':people.cpf,
            'income':people.income,
            'score':people.score,
            'status':people.status,

        }})

    def delete(self, id):
        people = Generate.query.get(id)
        db.session.delete(people)
        db.session.commit()

people_view = GenerateView.as_view('people_view')
app.add_url_rule(
    '/soli.ta/', view_func=people_view, methods=['POST']
)
app.add_url_rule(
    '/soli.co/<int:id>', view_func=people_view, methods=['GET']
)
app.add_url_rule(
    '/soli.co/', view_func=people_view, methods=['GET'],
)
app.add_url_rule(
    '/del.te/', view_func=people_view, methods=['DELETE'],
)