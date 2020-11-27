import json
from flask import request, jsonify, Blueprint, abort, render_template, redirect
from flask.views import MethodView
from my_app import db, app
from my_app.generate.models import Generate

generate = Blueprint('generate', __name__)

@generate.route('/')
def home():
    return render_template('index.html')

@generate.route('/soli.ta/', methods=['GET', 'POST'])
def requests():
    if request.method == 'POST':
        name = request.form['name']
        year = int(request.form['year'])
        cpf = int(request.form['cpf'])
        income = int(request.form['income'])
        methodic = GenerateView()
        id_url = methodic.post(name, year, cpf, income)
        url = 'http://127.0.0.1:5000/soli.co/{}'.format(id_url)
        return redirect(url, code=302)
    return render_template('solicitar.html')

@generate.route('/soli.co/', methods=['GET'])
def getRequest():
    methodic =  GenerateView()
    jsn = methodic.get()
    return jsn

@generate.route('/soli.co/<int:id>', methods=['GET'])
def getOneRequest(id):
    methodic =  GenerateView()
    jsn = methodic.get(id=id)
    return jsn

'''@generate.route('/soli.co/', methods=['GET', 'POST'])
def getRequest():
    methodic =  GenerateView()
    jsn = methodic.get()
    print(jsn)
    return render_template('solicitacao.html', json_values=jsn)'''

@generate.route('/del.te/', methods=['GET', 'POST'])
def deletePage():
    if request.method == 'POST':
        id = request.form['id']
        methodic =  GenerateView()
        people = methodic.delete(id)
        status = 'Status: O cliente {} do cpf: {}, foi excluido da base de dados.'.format(people.name, people.cpf)
        return render_template('delete.html', status=status)
    return render_template('delete.html', status='')

@generate.route('/del.te/<int:id>', methods=['GET', 'POST'])
def deleteRequest(id):
        methodic =  GenerateView()
        people = methodic.delete(id)
        status = 'Status: O cliente {} do cpf: {}, foi excluido da base de dados.'.format(people.name, people.cpf)
        return render_template('delete.html', status=status)


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

    def post(self, name, year, cpf, income):
        '''name = request.form.get('name')
        year = request.form.get('year')
        cpf = request.form.get('cpf')
        income = request.form.get('income')'''
        people = Generate(name, year, cpf, income)
        db.session.add(people)
        db.session.commit()
        return people.id

    def delete(self, id):
        people = Generate.query.get(id)
        db.session.delete(people)
        db.session.commit()
        return people


