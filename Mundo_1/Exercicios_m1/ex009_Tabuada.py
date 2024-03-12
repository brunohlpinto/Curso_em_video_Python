nr = int(input('nr para saber a sua tabuada: '))
t1 = nr*1
t2 = nr*2
t3 = nr*3
t4 = nr*4
t5 = nr*5
t6 = nr*6
t7 = nr*7
t8 = nr*8
t9 = nr*9
t10 = nr*10
cores = {'fim': '\033[m',
         'nr': '\033[30:45m',
         't': '\033[7:30:45m'}
print('a tabuada é: \n{}{}{} * 1 = {}{}{}'.format(cores['nr'], nr, cores['fim'], cores['t'], t1, cores['fim']))
print('{}{}{} * 2 = {}{}{}'.format(cores['nr'], nr, cores['fim'], cores['t'], t2, cores['fim']))
print('{}{}{} * 3 = {}{}{}'.format(cores['nr'], nr, cores['fim'], cores['t'], t3, cores['fim']))
print('{}{}{} * 4 = {}{}{}'.format(cores['nr'], nr, cores['fim'], cores['t'], t4, cores['fim']))
print('{}{}{} * 5 = {}{}{}'.format(cores['nr'], nr, cores['fim'], cores['t'], t5, cores['fim']))
print('{}{}{} * 6 = {}{}{}'.format(cores['nr'], nr, cores['fim'], cores['t'], t6, cores['fim']))
print('{}{}{} * 7 = {}{}{}'.format(cores['nr'], nr, cores['fim'], cores['t'], t7, cores['fim']))
print('{}{}{} * 8 = {}{}{}'.format(cores['nr'], nr, cores['fim'], cores['t'], t8, cores['fim']))
print('{}{}{} * 9 = {}{}{}'.format(cores['nr'], nr, cores['fim'], cores['t'], t9, cores['fim']))
print('{}{}{} * 10 = {}{}{}'.format(cores['nr'], nr, cores['fim'], cores['t'], t10, cores['fim']))

# tambem posso usar:
# print('{:2} * {:2} = {:2}'.format(nr, 1, nr*1)
