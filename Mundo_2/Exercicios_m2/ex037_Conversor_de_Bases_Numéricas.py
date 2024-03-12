nr = int(input('digite um nr: '))
print('escolha uma das seguintes opcoes para conversao: ')
print('[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal')
escolha = int(input('digite a sua escolha: '))

if escolha == 1:
    print('o nr {} em binario e: {}'.format(nr, bin(nr)[2:]))
elif escolha == 2:
    print('o nr {} em octal e: {}'.format(nr, oct(nr)[2:]))
elif escolha == 3:
    print('o nr {} em hexadecimal e: {}'.format(nr, hex(nr)[2:]))
else:
    escolha = int(input('digite a sua escolha entre 1, 2 ou 3: '))
# utilizar o fatiamento da string [2:]
# neste caso so quero que me de sem os dois primeiros digitos
