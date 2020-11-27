from my_app import db
from my_app.create.controller import generateScore, statusScore

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    year = db.Column(db.Integer)
    cpf = db.Column(db.String(255))
    income = db.Column(db.Integer)
    score = db.Column(db.String(255))
    status = db.Column(db.String(255))

    def __init__(self, name, year, cpf, income):
        self.name = name
        self.year = year
        self.cpf = cpf
        self.income = income
        self.score = generateScore()
        self.status = statusScore(self.score, self.income)

    def __repr__(self):
        return '<ID %d>'%self.id