import random 

def generate_score():
    score = random.randint(1, 999)
    return score

def status_score(score, renda):
    status=None
    if score<=299:
        status = 'Reprovado'
    elif score<=599:
        status='Aprovado, Limite de R$1000'
    elif score<=799:
        if renda>=1000:
            status='Aprovado, Limite de R${:.2}'.format(str(renda*(50/100)))
        else:
            status='Aprovado, Limite de R$1000 apenas, sua renda é abaixo de R$1000'
    elif score>799:
        status='Aprovado, Limite de R${:.2}'.format(str(renda*(200/100)))
    elif renda>1000000:
        status='Aprovado, Sem limite'
    return status
