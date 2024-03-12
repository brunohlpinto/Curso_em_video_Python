lista_final = []
lista_pares = []
lista_impares = []

for v in range(1, 8):
    num = int(input(f'Digite o {v}º valor: '))
    if num % 2 == 0 and num != 0:
        lista_pares.append(num)
        lista_pares.sort()
    elif num % 2 != 0 and num != 0:
        lista_impares.append(num)
        lista_impares.sort()
lista_final.append(lista_pares)
lista_final.append(lista_impares)
print(lista_final[:])
