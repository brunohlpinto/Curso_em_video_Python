# ver tambem solução do GG, bastante engenhosa
from time import sleep


def cabecalho(msg=''):
    print('\033[30;42m=\033[m'*len(msg))
    print(f'\033[30;42m{msg}\033[m')
    print('\033[30;42m=\033[m'*len(msg))


def fim(despedida=''):
    print('\033[30;46m=\033[m' * len(despedida))
    print(f'\033[30;46m{despedida}\033[m')
    print('\033[30;46m=\033[m' * len(despedida))


def python_help(escolha):
    espera = f'  A aceder ao manual {escolha}  '
    print('\033[30;41m=\033[m' * len(espera))
    print(f'\033[30;41m{espera}\033[m')
    print('\033[30;41m=\033[m' * len(espera))
    sleep(1)
    return help(escolha)


while True:
    cabecalho('  Sistema de ajuda Python  ')
    opcao = input('Função ou Biblioteca (escreva "fim" para sair): ')
    if opcao.lower() == 'fim':
        break
    python_help(opcao)

fim('  Finito  ')
