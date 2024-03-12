# regra 3 simples
preco1 = float(input('o preço original do produto é: '))
precofinal = preco1 - (preco1 * 0.05)
print('com o desconto, o preço final vai ficar {}{}{}'.format('\033[7:30:47m', precofinal, '\033[m'))
# ou
# preco final = preco1 - (preco1 * 5/100)
