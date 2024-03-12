total = produtos1000 = 0
menor = 0
cont = 0
barato = ''
while True:
    produto = str(input('qual e o produto: '))
    preco = float(input('qual e o preco?: $ '))
    cont += 1
    total = total + preco
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('quer continuar? S/N: ')).upper().strip()[0]
    if preco > 1000:
        produtos1000 += 1
    if pergunta == 'N':
        break

print('fim das compras')
print(f'o total gasto nas compras foi {total:.2f}$')
print(f'houve {produtos1000} produtos acima de 1000$')
print(f'o produto com menor preco foi {barato} com o preco de {menor:.2f}')
