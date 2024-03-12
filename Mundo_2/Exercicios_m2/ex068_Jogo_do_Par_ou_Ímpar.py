from random import randint

cabecalho = 'JOGO DO PAR OU IMPAR'
print("=" * (len(cabecalho) + 6))
print(f'   {cabecalho}')
print("=" * (len(cabecalho) + 6))

cont1 = 0
cont2 = 0

while True:
    num = int(input('Digite um valor: '))
    pc = randint(1, 10)
    total = num + pc
    p = ' '
    while p not in 'PI':
        p = str(input('par ou impar? P/I: ')).upper().strip()[0]

    if total % 2 == 0:
        print(f'voce jogou {num} e o computador jogou {pc}. o total deu {total} par')
    else:
        print(f'voce jogou {num} e o computador jogou {pc}. o total deu {total} impar')

    if p in 'Pp' and total % 2 == 0 or p in 'Ii' and total % 2 != 0:
        cont1 += 1
        print('voce ganhou')
    elif p in 'Pp' and total % 2 != 0 or p in 'Ii' and total % 2 == 0:
        cont2 += 1
        print('voce perdeu')
        break
    print('vamos jogar novamente...')
print(f'GAME OVER! voce venceu {cont1} vezes')
