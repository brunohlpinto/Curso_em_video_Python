from random import randint

nrs = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10))

maior = menor = 0

for n in range(0, len(nrs)):
    print(f'{n}', end=' ')
    if n == 0:
        maior = nrs[n]
        menor = nrs[n]
    else:
        if nrs[n] > maior:
            maior = nrs[n]
        if nrs[n] < menor:
            menor = nrs[n]
print(f'\nO menor nr é {menor}.')
print(f'O maior nr é {maior}.')
