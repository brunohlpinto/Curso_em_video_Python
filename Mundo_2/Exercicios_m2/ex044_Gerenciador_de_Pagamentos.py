print('{:=^40}'.format(' LOJA GUANABARA '))
# o alinhamento ficou ao centro e com o sina '=' dos lados
preco = float(input('digite o valor das compras: $ '))
print('''QUAL A OPÇAO DE PAGAMENTO?
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista cartao
[ 3 ] 2x no cartao
[ 4 ] 3x ou mais no cartao''')
# usar ''' para utilizar mais linhas
opcao = float(input('opcao: '))
preco_final = preco

if opcao == 1:
    preco_final = preco - (preco*10/100)
elif opcao == 2:
    preco_final = preco - (preco*5/100)
elif opcao == 3:
    prestacoes = preco / 2
    print('a sua compra sera parcelado em 2x de {}'.format(prestacoes))
elif opcao == 4:
    prestacoes = int(input('quantas prestacoes?: '))
    preco_final = preco + (preco*20/100)
    print('a sua compra sera parcelada em {}x de {:.2f} com juros'.format(prestacoes, (preco_final/prestacoes)))
else:
    print('opcao invalida')
print('a sua compra de {:.2f} vai custar no final {:.2f}'.format(preco, preco_final))
