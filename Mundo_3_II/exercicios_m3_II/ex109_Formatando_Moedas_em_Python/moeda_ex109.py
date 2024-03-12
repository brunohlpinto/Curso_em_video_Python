import fmoeda_ex109


# Programa principal
# utilizar float para converter o numero das funcoes metade, dobro, ... em float
# antes de chegar à função moeda

# 1º print diferente / experiência
# o primeiro print não tem porque na função metade coloquei a retornar um valor float
preco = float(input('Digite um preço: $ '))
print(f'A metade de {fmoeda_ex109.moeda(preco)} é {fmoeda_ex109.metade(preco, False)}')
print(f'O dobro de {fmoeda_ex109.moeda(preco)} é {fmoeda_ex109.dobro(preco, False)}')
print(f'Com aumento de 10%, o valor final é {fmoeda_ex109.aumentar(preco, 10, False)}')
print(f'Com diminuição de 13%, o valor final é {fmoeda_ex109.diminuir(preco, 13, True)}')
