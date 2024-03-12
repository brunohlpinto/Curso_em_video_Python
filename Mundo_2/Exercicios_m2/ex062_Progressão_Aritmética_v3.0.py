n = int(input('primeiro termo: '))
r = int(input('razao: '))
n2 = n
cont = 1
total = 0
m = 10
while m != 0:
    total = total + m
    while cont <= total:
        # usar estrutura aninhada
        # criar uma variavel para saber input de quantos termos, mas com a contagem ja no 10 do primeiro exercicio
        # criar uma variavel com total = 0 para saber no final quantos termos foram pedidos
        print('{} -> '.format(n2), end='')
        n2 += r
        n2 += r
        cont += 1
    print('pausa')
    m = int(input('quantos termos quer ver mais?: '))
print(f'programa terminado com {total} termos pedidos')