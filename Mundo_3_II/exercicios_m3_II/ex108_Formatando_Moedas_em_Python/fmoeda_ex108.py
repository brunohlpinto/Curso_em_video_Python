def metade(p):
    return float(f'{(p / 2):.2f}')
# experiencia
# a def metade é a única que retorna um valor float
# dessa forma não é preciso colocar no programa principal
# tal como vai acontecer com as outras


def dobro(p):
    return f'{(p * 2):.2f}'


def aumentar(p, percentagem):
    return f'{p + (p * percentagem/100):.2f}'


def diminuir(p, percentagem):
    return f'{p - (p * percentagem/100):.2f}'


def moeda(p):
    return f'E${p:.2f}'.replace('.', ',')
# replace para trocar '.' por ','


# solução GG
"""def metade(p=0):
    res = p / 2
    return res


def dobro(p=0):
    res = p * 2
    return res


def aumentar(p=0, percentagem=0):
    res = p + (p * percentagem / 100)
    return res 


def diminuir(p=0, percentagem=0):
    res = p - (p * percentagem / 100)
    return res 


def moeda(p=0, moeda ='E$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')"""

