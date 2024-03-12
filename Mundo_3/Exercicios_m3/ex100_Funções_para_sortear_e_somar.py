from random import randint
from time import sleep

numeros = []


def sorteia(*valores):
    print('Os 5 valores sorteados da lista são:', end=' ')
    for num in valores:
        numeros.append(num)
        print(num, end=' ')
        sleep(0.5)
    print('FIM!')


def soma_pares(*valores):
    soma = 0
    for nums in valores:
        for v in nums:
            if v % 2 == 0:
                soma += v
    print(f'A soma dos valores pares da lista {nums} é: {soma}')


sorteia(randint(1, 10), randint(1, 10),
        randint(1, 10), randint(1, 10), randint(1, 10))
soma_pares(numeros)
