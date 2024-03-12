def leiaint(prompt=''):
    while True:
        try:
            entrada = int(input(prompt))
        except:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            break
    return int(entrada)


"""# Solução GG a utilizar continue
def leiaint(prompt=''):
    while True:
        try:
            entrada = int(input(prompt))
        except:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return int(entrada)"""


def leiafloat(prompt=''):
    while True:
        try:
            entrada2 = input(prompt)
            if entrada2 == str(''):
                entrada2 = 0
            else:
                entrada2 = float(entrada2)
        except:
            print(f'\033[1;31mERRO! Digite um número real válido. \033[m')
        else:
            break
    return float(entrada2)


"""# Solução GG para o return 0
# tenho que especificar quais as exceções antes da exceção KeyboardInterrupt para funcionar e retornar 0
def leiafloat(prompt=''):
    while True:
        try:
            entrada2 = float(input(prompt))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um número real válido. \033[m')
            continue
        except KeyboardInterrupt:
            print('O utilizador não digitou nr')
            return 0
        else:
            return float(entrada2)"""


# Programa principal
num = leiaint('Digite um número inteiro: ')
num2 = leiafloat('Digite um número real: ')
print(f'O número inteiro foi {num} e o número real foi {num2}')
