km = int(input('quantidade de kms percorridos: '))
d = int(input('quantidade de dias alugado: '))
preco = (km*0.15) + (d*60)
print('percorreu {}{}{}km em {}{}{} dias. o preço a pagar será {}{:.2f}{}R$'.format('\033[31:107m', km, '\033[m',
                                                                                    '\033[7:31:107m', d, '\033[m',
                                                                                    '\033[32:40m', preco, '\033[m'))
# modalizar o codigo / dividir para conquistar
# ir testando por partes
# dividir em pedaços / em pequenas tarefas
# por exemplo: 1º ver os km e depois os km e dias
