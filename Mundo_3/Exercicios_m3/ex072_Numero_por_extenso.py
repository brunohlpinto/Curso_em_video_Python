nrs = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'catorze', 'quinze',
       'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')

while True:
    nr = int(input('digite um nr de 0 a 20: '))
    if 0 <= nr <= 20:
        break
    else:
        print('erro', end='')
print(f'O nr escolhido por extenso é {nrs[nr]}.')
