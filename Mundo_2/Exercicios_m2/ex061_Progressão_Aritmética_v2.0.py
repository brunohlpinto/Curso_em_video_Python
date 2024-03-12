n = int(input('primeiro termo: '))
r = int(input('razao: '))
pa = n + ((10-1) * r)
n2 = n
cont = 1
while cont <= 10:
    print('{} -> '.format(n2), end='')
    n2 += r
    cont += 1
print('fim')
