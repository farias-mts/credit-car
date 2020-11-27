import random 

def generateScore():
    score = random.randint(1, 999)
    return score

def statusScore(score, renda):
    status=None
    if score<=299:
        status = 'Reprovado'
    elif score<=599:
        status='R$1000'
    elif score<=799 and renda>=1000:
        status=str(renda*(50/100))
    elif score<=799:
        status=str(renda*(200/100))
    elif renda>1000000:
        status='Sem limite'
    return status