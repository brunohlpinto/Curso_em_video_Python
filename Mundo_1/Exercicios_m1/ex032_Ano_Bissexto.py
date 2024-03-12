# solucao mais simples
from datetime import date
ano = int(input('Que ano quer analisar: '))
cores = {'fim': '\033[m',
         'b': '\033[1:4:35m',
         'nb': '\033[7:1:4:35m'}
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano de {}{}{} e {}bissexto{}'.format(cores['b'], ano, cores['fim'], cores['b'], cores['fim']))
else:
    print('o ano de {}{}{} {}nao e bissexto{}'.format(cores['nb'], ano, cores['fim'], cores['nb'], cores['fim']))

# minha solucao
# feito mas com muitas linhas de codigo
""" import datetime
data = int(input('Que ano quer analisar? Coloque 0 para o ano actual: '))
actual = (0 == datetime.datetime.now().year)

if data == 0:
    print('o ano actual e {}'.format(datetime.datetime.now().year))
else:
    print('o ano escolhido foi {}'.format(data))

if data and actual % 4 == 0 and data % 100 !=0 or data and actual % 400 == 0:
    print('o ano e bissexto')
else:
    print('o nao e bissexto') """
