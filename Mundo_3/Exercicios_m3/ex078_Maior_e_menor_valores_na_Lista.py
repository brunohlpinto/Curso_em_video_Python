lista = list()
maior = menor = 0

for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print(f'Digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
