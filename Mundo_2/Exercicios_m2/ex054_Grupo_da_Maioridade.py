from datetime import date
maior = 0
menor = 0

for p in range(1, 8):
    nascimento = int(input(('em que ano a {}ª pessoa nasceu?: '.format(p))))
    ano_actual = date.today().year
    idade = ano_actual - nascimento
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('teve {} pessoas maior de idade'.format(maior))
print('teve {} pessoas menores de idade'.format(menor))
