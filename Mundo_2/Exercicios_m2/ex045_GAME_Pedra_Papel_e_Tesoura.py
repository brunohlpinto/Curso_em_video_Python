from time import sleep
from random import randint

# solucao guanabar
# devia ter utilizado modulos, ver ex019 e ex020
# so utilizei if e elif, demasiado complicado

itens = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)
print('''opcoes:
[ 0 ] Pedra 
[ 1 ] Papel 
[ 2 ] Tesoura''')
escolha = int(input('Qual a sua escolha?: '))

print('pedra')
sleep(1)
print('papel')
sleep(1)
print('tesoura')
sleep(1)

print('-=' * 10)
print('o pc jogou {}'.format(itens[pc]))
print('o jogador jogou {}'.format(itens[escolha]))
print('-=' * 10)

if pc == 0:  # computador jogou pedra
    if escolha == 0:
        print('empate')
    elif escolha == 1:
        print('jogador vence')
    elif escolha == 2:
        print('pc vence')
    else:
        print('opcao invalida')
elif pc == 1:
    if escolha == 0:
        print('pc vence')
    elif escolha == 1:
        print('empate')
    elif escolha == 2:
        print('jogador vence')
    else:
        print('opcao invalida')
elif pc == 2:
    if escolha == 0:
        print('jogador vence')
    elif escolha == 1:
        print('pc vence')
    elif escolha == 2:
        print('empate')
    else:
        print('opcao invalida')
