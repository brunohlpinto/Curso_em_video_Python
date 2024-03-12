from math import radians, sin, cos, tan
an = float(input('digite o valor do angulo: '))
seno = sin(radians(an))
print('o angulo de {}{}{} tem o seno de {}{:.2f}{}'.format('\033[7:34:40m', an, '\033[m',  '\033[35:40m', seno, '\033[m'))
cosseno = cos(radians(an))
print('o angulo de {}{}{} tem o cosseno de {}{:.2f}{}'.format('\033[7:34:40m', an, '\033[m', '\033[7:35:40m', cosseno, '\033[m'))
tangente = tan(radians(an))
print('o angulo de {}{}{} tem a tangente de {}{:.2f}{}'.format('\033[7:34:40m', an, '\033[m', '\033[36:40m', tangente, '\033[m'))

""" import math
an = float(input('digite o valor do angulo: '))
seno = math.sin(math.radians(an))
print('o angulo de {} tem o seno de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('o angulo de {} tem o cosseno de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('o angulo de {} tem a tangente de {:.2f}'.format(an, tangente)) """