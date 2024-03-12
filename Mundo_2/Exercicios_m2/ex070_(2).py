cont = total = cont1000 = menor = 0
while True:
    produto = str(input('digite o produto: '))
    preco = float(input('digite o preco: '))
    cont += 1
    total += preco
    nomemenor = ''
    if cont == 1:
        menor = preco
        nomemenor = produto
    else:
        if preco < menor:
            menor = preco
            nomemenor = produto
    if preco > 1000:
        cont1000 += 1
    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = str(input('quer continuar? S/N: ')).lower().strip()[0]
    if pergunta == 'n':
        break
print('fim das compras')
print(f'o total gasto nas compras foi {total:.2f}$')
print(f'houve {cont1000} produtos acima de 1000$')
print(f'o nome do produto mais barato e {nomemenor}')
