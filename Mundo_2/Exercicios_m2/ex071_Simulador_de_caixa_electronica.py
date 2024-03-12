print('='*40)
print('{:^40}'.format('Banco Curso em Video'))
print('='*40)

ced50 = ced10 = ced1 = 0

while True:
    dinheiro = int(input('quanto dinheiro quer levantar?: $ '))
    if dinheiro >= 50:
        ced50 = dinheiro // 50
        if ced50 >= 1:
            print(f'total de {ced50} notas de 50')
    if dinheiro >= 10:
        ced10 = (dinheiro % 50 // 10)
        if ced10 >= 1:
            print(f'total de {ced10} notas de 10')
    if dinheiro >= 1:
        ced1 = (dinheiro % 10) // 1
        if ced1 >= 1:
            print(f'total de {ced1} notas de 1')
    break
print('Volte sempre ao Banco CEV. Tenha um bom dia!')
