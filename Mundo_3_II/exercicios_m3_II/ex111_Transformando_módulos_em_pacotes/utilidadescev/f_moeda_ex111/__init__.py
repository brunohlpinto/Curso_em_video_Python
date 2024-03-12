def cabecalho(txt):
    return txt


def metade(p=0, f=False):
    res = p / 2
    return moeda(res) if f is True else res


def dobro(p=0, f=False):
    res = p * 2
    return moeda(res) if f is True else res


def aumentar(p=0, percentagem=0, f=False):
    res = p + (p * percentagem / 100)
    return moeda(res) if f is True else res


def diminuir(p=0, percentagem=0, f=False):
    res = p - (p * percentagem / 100)
    return moeda(res) if f is True else res


def moeda(p=0.0, moedasimb='E$'):
    return f'{moedasimb}{p:.2f}'.replace('.', ',')


def linha(txt):
    return '-'*len(txt)


def resumo(p=0, a=0, d=0):
    print('-'*30)
    print(cabecalho('Resumo'.center(30)))
    print('-'*30)
    # \t é tabulação
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Metade do preço: \t{moeda(metade(p))}')
    print(f'Dobro do preço: \t{moeda(dobro(p))}')
    print(f'{a}% de aumento: \t{moeda(aumentar(p, a))}')
    print(f'{d}% de diminuição: \t{moeda(diminuir(p, d))}')
    print('-' * 30)
    