def moeda(p=0.0, moedasimb='E$'):
    return f'{moedasimb}{p:.2f}'.replace('.', ',')


def metade(p=0.0, f=True):
    if not f:
        p = p / 2
    if f:
        p = moeda(p / 2)
    return p


def dobro(p=0.0, f=True):
    if not f:
        p = p * 2
    if f:
        p = moeda(p * 2)
    return p


def aumentar(p=0.0, percentagem=0.0, f=True):
    if not f:
        aumento = p + (p * percentagem / 100)
    if f:
        aumento = moeda(p + (p * percentagem / 100))
    return aumento


def diminuir(p=0.0, percentagem=0, f=True):
    if not f:
        diminuicao = p - (p * percentagem / 100)
    if f:
        diminuicao = moeda(p - (p * percentagem / 100))
    return diminuicao


# solução GG
# mais simples
"""def metade(p=0, f=False):
    res = p / 2
    return res if f else moeda(res)
    # ou return res if f is False else moeda(res)
    # ou return res if not f else moeda(res)


def dobro(p=0, f=False):
    res = p * 2
    return res if f else moeda(res)


def aumentar(p=0, percentagem=0, f=False):
    res = p + (p * percentagem / 100)
    return res if f else moeda(res)


def diminuir(p=0, percentagem=0, f=False):
    res = p - (p * percentagem / 100)
    return res if f else moeda(res) 


def moeda(p=0, moeda ='E$', f=False):
    return f'{moeda}{p:.2f}'.replace('.', ',')"""
