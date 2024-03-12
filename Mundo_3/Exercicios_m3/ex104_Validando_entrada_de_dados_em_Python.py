import builtins


def leiaint(prompt=''):
    while True:
        entrada = builtins.input(prompt)
        if not entrada.isnumeric():
            print('\033[1;31mERRO! Digite um número válido.\033[m')
        else:
            break
    return int(entrada)


# Programa principal
num = leiaint('Digite um número: ')
print(f'Digitou o nr {num}!')

# podia ter feito com o input mesmo e escusava de utilizar e importar builtins ou prompts
