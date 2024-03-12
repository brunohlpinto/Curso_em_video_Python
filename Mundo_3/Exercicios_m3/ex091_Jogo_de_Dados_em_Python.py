from random import randint
from operator import itemgetter

jogadores = {'player1': randint(1, 7), 'player2': randint(1, 7),
             'player3': randint(1, 7), 'player4': randint(1, 7)}
# solucao GG
# criar outro dicionario
ranking = dict()

for j, c in jogadores.items():
    print(f'O {j} tirou {c} no dado.')

print('='*20)
print(f'{'--- Ranking ---':^20}')

# solucao GG
# criar outro dicionario

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')

# minha solução para a segunda parte do problema
# mas nao apareceu o player
"""for p, d in enumerate(sorted(jogadores.values(), reverse=True)):
    print(f'{p+1}º lugar: com {d}')"""
