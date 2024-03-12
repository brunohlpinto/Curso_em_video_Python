def metade(p):
    return f'{(p / 2):.2f}'


def dobro(p):
    return f'{(p * 2):.2f}'


def aumentar(p, percentagem):
    return f'{p + (p * percentagem/100):.2f}'


def diminuir(p, percentagem):
    return f'{p - (p * percentagem/100):.2f}'
