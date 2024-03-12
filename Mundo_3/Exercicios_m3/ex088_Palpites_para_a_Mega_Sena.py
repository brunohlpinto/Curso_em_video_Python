from random import randint

jogadas = int(input('Quantos jogos quer sortear?: '))

for i in range(jogadas):
    lista_jogo = []

    while len(lista_jogo) < 5:
        num = randint(1, 60)
        if num not in lista_jogo:
            lista_jogo.append(num)

    print(lista_jogo)
