num = int(input('digite um nr (utilize 999 para parar): '))
# podia ter feito com o num o mesmo que os contadores
# num = 0
cont = 0
cont2 = 0
while num != 999: # enquanto o nr nao for 999 vai printar:
    cont = cont + num # os contadores vem primeiro, antes do num
    cont2 += 1 #
    num = int(input('digite um nr (utilize 999 para parar): '))
    # ao ficar em ultimo os contadores nao vao contar o 999, tanto para o cont como o cont2
# quando for 999 vai printar o seguinte:
print(f'foram digitados {cont2} avalores e a soma entre eles foi de {cont}')