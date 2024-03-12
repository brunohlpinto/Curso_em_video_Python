from datetime import date
nascimento = int(input('Ano de nascimento: '))
ano_actual = date.today().year
idade = ano_actual - nascimento

if idade < 18:
    print('quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, ano_actual))
    print('tem que se alistar em {} anos'.format(18-idade))
elif idade == 18:
    print('quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, ano_actual))
    print('tem que se alistar este ano')
else:
    print('quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, ano_actual))
    print('ja se deveria ter alistado a {} anos'.format(idade-18))
