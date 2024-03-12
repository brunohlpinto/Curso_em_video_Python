# minha solução
lista1 = []

for v in range(1, 10):
    lista1.append(int(input('Digite um valor: ')))

for i, valor in enumerate(lista1):
    if i <= 2:
        print(f'[ {valor:^5} ]', end=' ')
        if i == 2:
            print()
    elif i <= 5:
        print(f'[ {valor:^5} ]', end=' ')
        if i == 5:
            print()
    elif i <= 8:
        print(f'[ {valor:^5} ]', end=' ')

# solução GG

""" matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(0, 3):
    for l in range(0, 3):
        matriz[c][l] = int(input(f'Digite para {c}, {l}: '))

for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print() """
