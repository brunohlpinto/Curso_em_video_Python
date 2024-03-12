n = int(input('digite nr para calcular facturial: '))
c = n
f = 1
print('calcular {}! = '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f), end='')

""" from math import factorial
n = int(input('digite nr para calcular facturial: '))
f = factorial(n)
print('o factorial de {} e = {}'.format(n, f) """

# com o for

""" n = int(input('Digite um numero para calcular o seu fatorial: '))
f = 1
print(f'Calculando {n}! = ', end='')
for c in range(n, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f'{f}') """