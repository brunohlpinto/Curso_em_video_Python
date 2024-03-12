print('-- Fatorial --')


def fatorial(num, show=True):
    """
    -> Serve para calcular o fatorial de um numero
    :param num: recebe input do numero para calcular
    :param show: True or False para escolher ver a conta que levou ao fatorial ou não
    :return: retorna o valor do fatorial de num
    """
    f = 1
    print('*' * 50)
    if show:
        for v in range(num, 0, -1):
            f = f * v
            print(f'{v}', end=' ')
            if v > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        return f
    else:
        for v in range(num, 0, -1):
            f = f * v
        return f'O fatorial de {num} é {f}'


nr = int(input('Digite um nr para saber o seu fatorial: '))
print(fatorial(nr, False))
help(fatorial)
