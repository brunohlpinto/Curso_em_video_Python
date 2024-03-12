lista1 = []

for v in range(1, 10):
    lista1.append(int(input('Digite um valor: ')))

cont = soma = maior = 0
for i, valor in enumerate(lista1):
    if valor % 2 == 0:
        cont = cont + valor
    if i <= 2:
        print(f'[ {valor:^5} ]', end=' ')
        if i == 2:
            print()
    elif i <= 5:
        print(f'[ {valor:^5} ]', end=' ')
        if i == 3:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        if i == 5:
            print()
    elif i <= 8:
        print(f'[ {valor:^5} ]', end=' ')
        soma = soma + valor
print()
print(f'A soma dos valores pares é {cont}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor da segunda coluna é {maior}')
