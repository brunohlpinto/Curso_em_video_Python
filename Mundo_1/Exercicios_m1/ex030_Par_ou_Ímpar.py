nr = int(input('Digite um nr para saber se e par ou imppar: '))

# minha soluçao
if nr % 2 == 0:
    print('{}{:<10}{}'.format('\033[7:1:4:33m', 'o nr e par', '\033[m'))
else:
    print('{}{:<10}{}'.format('\033[1:34m', 'o nr e impar', '\033[m'))

# tambem pode ser
""" resultado = nr % 2 == 0
print('o resultado e {}'.format(resultado)) """
