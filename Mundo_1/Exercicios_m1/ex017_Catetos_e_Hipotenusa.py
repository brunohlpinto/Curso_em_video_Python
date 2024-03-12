# usar o teorema de pitagoras para descobrir o comprimento da hipotenusa
from math import sqrt, pow
ca = float(input('digite o valor do cateto adjacente: '))
co = float(input('digite o valor do cateto oposto: '))
h = sqrt(pow(ca, 2) + pow(co, 2))
print('o valor do cateto adjacente é \033[33:40m{:.2f}\033[m, do cateto oposto é \033[7:33:40m{:.2f}\033[m e da hipotenusa é \033[34:40m{:.2f}\033[m'.format(ca, co, h))
# ou
# h = (ca**2 + co**2) ** (1/2)
# ou
# import math
# math.hypot(co, ca)
