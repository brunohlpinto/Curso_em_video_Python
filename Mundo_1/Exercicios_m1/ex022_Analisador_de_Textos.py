nomec = str(input('digite seu nome completo: ').strip())
print('Seu nome completo é : \033[7:37:40m{}\033[m'.format(nomec))
nomec_mai = nomec.upper()
print('seu nome completo em maisuculas é: \033[1:31:44m{}\033[m'.format(nomec_mai))
nomec_min = nomec.lower()
print('seu nome completo em minusculas é \033[7:1:31:44m{}\033[m'.format(nomec_min))

dividido = nomec.split()
letras = "".join(dividido)
print('o nr de letras na frase é \033[31:107m{}\033[m'.format(len(letras)))
print('o primeiro nome é \033[7:31:107m{}\033[m e tem \033[32:107m{}\033[m letras.'.format(dividido[0], len(dividido[0])))

# para contar as letras, tambeem pode ser:
# print('o nr de letras na frase é {}'.format(len(letras) - nomec.count(' ')))

# para contar as letras do primeiro nome poder ser:
# print('o primeiro nome tem {} letras'.format(nomec.find(' ')))
