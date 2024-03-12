equipa = list()
while True:
    jogador = dict()
    golos = list()
    tot = 0

    jogador["nome"] = input('Nome do jogador: ')
    jogos = int(input(f'Quantos jogos o {jogador["nome"]} jogou?: '))

    for g in range(1, jogos + 1):
        golos.append(int(input(f'   Quantos golos marcou no jogo {g}: ')))

    for go in golos:
        tot += go
    jogador['golos'] = golos[:]
    jogador['total'] = tot

    equipa.append(jogador.copy())

    print('-' * 50)
    while True:
        opcao = input('Quer continuar? S/N: ').strip().upper()
        if opcao in 'SN':
            break
        print('Erro. Responda S ou N')
    if opcao == 'N':
        break
print('-' * 50)

print('{:<3}'.format('Cod'), end=' ')
print('{:<20}'.format('Nome'), end='')
print('{:<20}'.format('Golos'), end='')
print('{:<20}'.format('Total'))

print('-' * 50)
for i, info in enumerate(equipa):
    print(f'{i:<4}', end='')
    print(f'{info["nome"]:<20}', end='')
    print(f'{str(info["golos"]):<20}', end='')
    # transformar a lista em string para poder fazer o print
    print(f'{info["total"]:<20}')
print('-' * 50)

while True:
    opcao2 = int(input('Mostrar dados de qual jogador? (prima 999 para sair): '))
    if opcao2 == 999:
        break
    for i, info in enumerate(equipa):
        if opcao2 == i:
            print(f'Levantamento do jogador {info['nome']}:')
            for j, g in enumerate(info['golos']):
                print(f'  --> No jogo {j + 1} fez {g} golos.')
            print('-' * 50)
        else:
            print('Número inválido')
print('Finito')
