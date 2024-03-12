met = float(input('valor em metros: '))
km = met * 0.001
hm = met * 0.01
dam = met * 0.1
dm = met * 10
cen = met * 100
mil = met * 1000
# este exercicio tem as 3 formas de colocacao de cores
cores = {'fim': '\033[m',
         'dm': '\033[7:30:43m',
         'cen': '\033[30:44m',
         'mil': '\033[7:30:44m'}

print('o valor em metros é \033[7:30:41m{}\033[m'.format(met))
print('o valor em km é {}{}{}\nem hectometros é {}{}{} \nem decametros é {}{}{}'.format('\033[30:42m', km, '\033[m',
                                                                                        '\033[7:30:42m', hm, '\033[m',
                                                                                        '\033[30:43m', dam, '\033[m'))
print('o valor em decimetros é {}{}{}\nem centimetros é {}{}{}\ne em milimetros é {}{}{}'.format(cores['dm'], dm, cores['fim'],
                                                                                                 cores['cen'], cen, cores['fim'],
                                                                                                 cores['mil'], mil, cores['fim']))
