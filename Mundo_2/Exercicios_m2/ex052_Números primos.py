n = int(input('digite um nr para saber se e nr primo: '))
primo = 0
cont = 0
for p in range(1, n+1):
    if n % p == 0:
        cont += 1
        print('\033[33m', p, '\033[m', end='')
    else:
        print('\033[31m', p, '\033[m', end='')
print('\no nr {} foi divisivel {} vezes'.format(n, cont, end=''))
if cont == 2:
    print('por isso e primo')
else:
    print('por isso nao e primo')
