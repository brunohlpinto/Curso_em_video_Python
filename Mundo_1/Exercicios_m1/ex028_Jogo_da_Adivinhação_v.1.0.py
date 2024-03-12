from random import randint
from time import sleep

nr = int(input('tente adivinhar um nr de 0 a 5: '))
print('o nr que escolheste foi {}{}{}'.format('\033[1:31m', nr, '\033[m'))
npc = randint(0, 5)  # faz o pc sortear um nr
# o pc espera 2 segundos antes de rodar o programa
# pode personalizar o tempo
# from time import sleep
sleep(2)
cores = {'fim': '\033[m',
         'certo': '\033[4:31m',
         'errado': '\033[1:4:32m'}
print('o nr certo e: {}{}{}'.format(cores['certo'], npc, cores['fim']))
if nr == npc:
    print('{}{:<20}{}'.format(cores['certo'], 'da lhe!!', cores['fim']))
else:
    print('{}{:<20}{}'.format(cores['errado'], 'tenta novamente maluco', cores['fim']))
