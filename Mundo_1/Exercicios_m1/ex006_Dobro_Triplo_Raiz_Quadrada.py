n = int(input('valor: '))
print('o nr escolhido foi {}{}{}, o dobro é {}{}{}, o triplo é {}{}{} e a sua raiz quadrada é {}{:.2f}{}.'.format(
                                                                                                            '\033[97:43m', n, '\033[m',
                                                                                                            '\033[97:44m', n*2, '\033[m',
                                                                                                            '\033[97:45m', n*3, '\033[m',
                                                                                                            '\033[97:46m', n**(1/2), '\033[m'))
# tambem posso usar:
# d = n*2
# t = n*3
# rq = n**(1/2)
# print(n,d,t,rq,rc)
# para a raiz quadradada pode ser .format(n, pow(n, (1/2)))
