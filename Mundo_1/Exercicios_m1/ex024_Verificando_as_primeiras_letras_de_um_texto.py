#colocar str antes do input
cidade = str(input('digite o nome da cidade: ')).strip()
print('a cidade ecolhida foi {}{}{}'.format('\033[7:35:107m', cidade, '\033[m'))

# fazer strip para eliminar espaços a direita e esquerda
# colocar os indices da frase que vamos precisar .upper
# e depois ver se é igual a 'SANTO' em maisuculas
print('\033[33:40m', cidade[:5].upper() == 'SANTO', '\033[m')
