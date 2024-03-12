import funcoes_moeda


# Programa principal
preco = float(input('Digite um preço: $ '))
print(f'A metade de {preco}$ é {funcoes_moeda.metade(preco)}$')
print(f'O dobro de {preco}$ é {funcoes_moeda.dobro(preco)}$')
print(f'Com aumento de 10%, o valor final é {funcoes_moeda.aumentar(preco, 10)}$')
print(f'Com diminuição de 13%, o valor final é {funcoes_moeda.diminuir(preco, 13)}$')
