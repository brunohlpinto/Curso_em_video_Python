vel = float(input('a que velocidade seguia: '))

# solucao com menos codigo / condicao simples
if vel > 80:
    print('multado. a velocidade a que seguia era \033[7:1:4:32m{:.1f}\033[m km/h. a sua multa é de \033[1:33m{:.1f}\033[m euros'.format(vel, ((vel - 80)*7)))
print('{}{:<10}{}'.format('\033[1:4:33m', 'boa viagem', '\033[m'))

# minha solucao
# esta certo mas nao precisava do else
""" if vel <= 80:
    print('a velocidade a que seguia era de {:.1f} km/h. boa viagem'.format(vel))
else:
    print('a velocidade a que seguia era {:.1f} km/h. a sua multa é de {:.1f} euros'.format(vel, ((vel - 80)*7))) """
