n = int(input('valor: '))
print('o nr escolhido é \033[97:40m{}\033[m, o seu antecessor é \033[97:41m{}\033[m e o sucessor é \033[97:42m{}\033[m.'.format(n, n-1, n+1))
# também posso criar:
# a = n-1
# s = n+1
# print(n,a,s)
