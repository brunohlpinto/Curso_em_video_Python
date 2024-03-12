cabecalho = 'REGISTE UMA PESSOA'
print("«»" * (len(cabecalho) + 6))
print(' ' * 12, cabecalho)
print("«»" * (len(cabecalho) + 6))

contidade18 = conthomem = contf20 = 0

while True:
    i = int(input('idade: '))
    s = ' '
    p = ' '
    while s not in 'MF':
        s = str(input('Sexo M/F: ')).strip().upper()[0]
    print('--' * (len(cabecalho) + 6))
    if i < 18:
        contidade18 += 1
    if s in 'Mm':
        conthomem += 1
    if s in 'Ff' and i < 20:
        contf20 += 1
    while p not in 'SN':
        p = str(input('quer continuar?: ')).strip().upper()[0]
    print('--' * (len(cabecalho) + 6))
    if p in 'Nn':
        break
print(f'existem {contidade18} pessoas com menos de 18 anos')
print(f'exitem {conthomem} homens')
print(f'exitem {contf20} mulheres com menos de 20 anos')
print('fim')
