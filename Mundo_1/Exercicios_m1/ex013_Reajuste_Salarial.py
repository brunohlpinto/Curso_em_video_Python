salariobase = float(input('o seu salario bruto era de: '))
aumento = salariobase + (salariobase * 0.15)
print('no entanto, vai ser aumentado. vai passar de \033[30:107m{:.2f} $\033[m brutos para um novo salário bruto de \033[7:30:107m{:.2f} $\033[m '.format(salariobase, aumento))
# ou
# aumento = salariobase + (salariobase * 15/100)
