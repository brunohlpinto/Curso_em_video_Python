kms = float(input('digite em kms a distancia que percorreu: '))
print('a distancia percorrida foi {}{}{}'.format('\033[1:4:34m', kms, '\033[m'))
km1 = kms * 0.50
km2 = kms * 0.45
if kms <= 200:
    print('o valor a pagar e de {}{:.2f}{} euros'. format('\033[7:1:4:34m', km1, '\033[m'))
else:
    print('o valor a pagar e de {}{:.2f}{} euros'.format('\033[1:35m', km2, '\033[m'))

# tambem pode ser
# fazer a condicao com a variavel / objeto
""" if kms <= 200:
    preco = kms * 0.5
else:
    preco = kms * 0.45
print('o valor a pagar e {:.2f}'.format(preco)) """
