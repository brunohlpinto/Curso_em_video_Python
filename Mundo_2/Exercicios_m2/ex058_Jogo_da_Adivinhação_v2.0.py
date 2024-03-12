from random import randint
pc = randint(0, 11)
print('sou o seu computador...\npensei num numero entre 0 10. Acha que consegue adivinhar?')
nr = int(input('qual e o seu palpite?: '))
cont = 1
while nr != pc:
    cont += 1
    if nr != pc:
        if nr == 0 or nr < pc:
            print('mais... tente outra vez')
            nr = int(input('qual e o seu palpite?: '))
        else:
            print('menos... tente outra vez')
            nr = int(input('qual e o seu palpite?: '))
print('boa, conseguiu acertar em {} tentativas'.format(cont))

# tambem pode ser
"""
from random import randint
computador = randint(0, 11)
print('sou o seu computador...\npensei num numero entre 0 10. Acha que consegue adivinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('qual e o seu palpite?: ')
    palpites += 1
    if jogador == computador:
    acertou = True
    else: 
        if: 
        jogador < computador:
        print('mais... tente outra vez')
        elif:
        jogador > computador:
        print('menos... tente outra vez')    
print('acertou com {} tentativas'.format(palpites))

"""