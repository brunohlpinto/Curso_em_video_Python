n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
nrs = (n1, n2, n3, n4)
print(f'Os números escolhidos foram {nrs}.')

cont9 = cont3 = contn3 = 0

print(f'O número 9 aparece {nrs.count(9)} vezes.')

for k in nrs:
    if k == 3:
        cont3 += 1
        if cont3 == 1:
            print(f'O valor 3 foi digitado na {nrs.index(3)+1}ª posição.')
for c in nrs:
    if c != 3:
        contn3 += 1
        if contn3 == 4:
            print('O valor 3 não foi digitado em nenhuma posição.')
# ou

""" if 3 in nrs:
    print(f'O valor 3 foi digitado na {nrs.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.') """

print('Os valores pares foram:', end=' ')
for p in nrs:
    if p % 2 == 0:
        print(p, end=' ')
