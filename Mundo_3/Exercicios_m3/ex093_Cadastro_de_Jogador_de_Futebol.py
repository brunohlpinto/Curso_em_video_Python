jogador = dict()
golos = list()

jogador['nome'] = input('Nome do jogador: ')
jogos = int(input(f'Quantos jogos o {jogador['nome']} jogou?: '))

tot = cont = 0

for g in range(1, jogos+1):
    golos.append(int(input(f'   Quantos golos marcou no jogo {g}: ')))

for go in golos:
    tot += go

jogador['golos'] = golos[:]
jogador['total'] = tot
print('-'*20)
print(jogador)
print('-'*20)

for i, k in jogador.items():
    print(f'O campo {i} tem o valor {k}')
print('-'*20)

print(f'O jogador {jogador['nome']} fez {len(jogador['golos'])} jogos.')
for j, g in enumerate(golos):
    print(f'  --> Na partida {j+1} fez {g} golos.')
print(f'Fez um total de {jogador['total']} golos.')
