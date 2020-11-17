from my_app import db

class Generate(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    year = db.Column(db.Integer)
    cpf = db.Column(db.Integer)
    income = db.Column(db.Integer)
    score = db.Column(db.Integer)
    status = db.Column(db.String(255))
    
    def __init__(self, name, year, cpf, income):
        from .controller import generate_score, status_score
        self.name = name
        self.year = year
        self.cpf = cpf
        self.income = income
        self.score = generate_score()
        self.status = status_score(self.score, self.income)

    def __repr__(self):
        return '<Id %d>' % self.id