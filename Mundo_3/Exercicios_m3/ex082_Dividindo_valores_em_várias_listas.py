valores = []
valores_pares = []
valores_impares = []

while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    if num % 2 == 0 and num != 0:
        valores_pares.append(num)
    elif num % 2 != 0 and num != 0:
        valores_impares.append(num)
    question = input('Quer continuar? S/N: ')
    while question not in 'SNsn':
        question = input('Quer continuar? S/N: ')
    if question == 'n':
        break
print(f'A lista é: {valores}')
print(f'A lista de valores pares é: {valores_pares}')
print(f'A lista de valores impares é: {valores_impares}')
