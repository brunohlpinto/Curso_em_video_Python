nr = int(input('digite um nr com maximo de 4 digitos: '))
print('Estamos a analisar o nr...')
string = str(nr)

# solução através da matemática
# fazer a divisão inteira por 1, 10, 100 e 1000 do nr e
# depois voltar a dividir por 10 de modo a ir buscar o resto da divisão
u = nr // 1 % 10
d = nr // 10 % 10
c = nr // 100 % 10
m = nr // 1000 % 10

cores = {'fim': '\033[m',
         'u': '\033[7:33:107m',
         'd': '\033[34:107m',
         'c': '\033[7:34:107m',
         'm': '\033[35:107m'}

print('{}unidade: {}{}'.format(cores['u'], u, cores['fim']))
print('{}dezena: {}{}'.format(cores['d'], d, cores['fim']))
print('{}centena: {}{}'.format(cores['c'], c, cores['fim']))
print('{}milhar: {}{}'.format(cores['m'], m, cores['fim']))
