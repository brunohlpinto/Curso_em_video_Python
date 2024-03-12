# solucao com mais codigo
# verificar quem e menor
n1 = int(input('digite o primeiro nr: '))
n2 = int(input('digite o segundo nr: '))
n3 = int(input('digite o terceiro nr: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificar que e maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('o menor nr e {}{}{}'.format('\033[1:30:107m', menor, '0\33[m'))
print('o maior nr e {}{}{}'.format('\033[7:1:30:107m', maior, '\033[m'))

# minha solucao
""" n1 = int(input('digite o primeiro nr: '))
n2 = int(input('digite o segundo nr: '))
n3 = int(input('digite o terceiro nr: '))

nrs = n1, n2, n3

print('dos tres escolhido, o menor nr e: {}'.format(min(nrs)))
print('dos tres escolhidos, o maior nr e: {}'.format(max(nrs))) """
