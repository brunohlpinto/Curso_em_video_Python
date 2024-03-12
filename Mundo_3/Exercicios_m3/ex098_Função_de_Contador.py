from time import sleep


def linha():
    print('='*35)


def contador(a, b, c):
    if c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    for z in range(a, b, c):
        print(z, end=' ')
        sleep(0.5)

    for z in range(a, b, -c):
        print(z, end=' ')
        sleep(0.5)

    print(b, end=' ')
    print('FIM!')
    linha()


# também dá para fazer com while

contador(1, 10, 1)
contador(10, 0, -2)

print('Personalize a contagem ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
