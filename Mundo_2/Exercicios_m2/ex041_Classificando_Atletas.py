from datetime import date
ano = int(input('ano de nascimento: '))
ano_actual = date.today().year
idade = ano_actual - ano

print('o atleta tem {} anos'.format(idade))

if idade <= 9:
    print('pertence a categoria mirim')
elif idade <= 14:
    print('pertence a categoria infantil')
elif idade <= 19:
    print('pertence a categoria junior')
elif idade <= 25:
    print('pertence a categoria senior')
else:
    print('pertence a categoria master')
