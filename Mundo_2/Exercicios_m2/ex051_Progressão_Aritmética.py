print('-'*10, ' 10 termos da PA ', '-'*10)
n = int(input('primeiro elemento: '))
r = int(input('razao: '))
f = n + (10-1) * r

for pa in range(n, f + r, r):
    print(pa, end=' -> ')
print('fim')
