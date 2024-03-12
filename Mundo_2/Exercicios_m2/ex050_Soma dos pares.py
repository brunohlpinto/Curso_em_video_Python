soma = 0
cont = 0
for y in range(1, 7):
    n = int(input('digite um valor: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('digitou {} valores pares e a soma entre eles e de {}'.format(cont, soma))
