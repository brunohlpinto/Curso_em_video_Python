casa = float(input('digite o valor da casa: $ '))
sal = float(input('digite o valor do seu salario: $ '))
anos = float(input('em quantos anos quer pagar o emprestimo: '))

empres = casa / (anos * 12)

if empres > (sal * 30 / 100):
    print('para pagar uma casa de {} $, com uma salario de {} $, em {} anos, '.format(casa, sal, anos), end='')
    print('a prestacao será de {:.2f} $ '.format(empres))
    print('emprestimo recusado')
elif empres <= (sal * 30 / 100):
    print('para pagar uma casa de {} $, com um salario de {} $, em {} anos, '.format(casa, sal, anos), end='')
    print('a prestacao será de {:.2f} $'.format(empres))
    print('emprestimo concedido')
