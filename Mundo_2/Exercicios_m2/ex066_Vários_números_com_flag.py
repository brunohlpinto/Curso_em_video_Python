cont = soma = 0

while True:
    num = int(input('digite um nr (999 para terminar): '))
    if num == 999:
        break
    cont += 1
    soma = soma + num
print('fim')
print(f'a quantidade de nrs digitados foi {cont} e a soma entre eles foi de {soma}')
