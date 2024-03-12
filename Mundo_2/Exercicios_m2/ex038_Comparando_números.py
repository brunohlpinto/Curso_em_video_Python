n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))

if n1 > n2:
    print('o primeiro valor e maior')
elif n2 > n1:
    print('o segundo valor e maior')
elif n1 == n2: # ou else (nao ha uma 4 opcao)
    print('nao existe valor maior, os dois sao iguais')
