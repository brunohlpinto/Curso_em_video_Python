salario = float(input('digite o valor do seu ordenado: $ '))
cores = {'salario': '\33[1:41m',
         'aumento': '\033[4:34m',
         'fim': '\033[m'}
if salario <= 1250:
    aumento = salario + (salario * 0.15)  # ou 15/100
else:
    aumento = salario + (salario * 0.10)  # ou 10/100
print('quem ganhava {}{:.2f}{} $, passa a receber {}{:.2f}{} $'.format(cores['salario'], salario, cores['fim'], cores['aumento'], aumento, cores['fim']))
