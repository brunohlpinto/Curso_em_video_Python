r = 'S'
cont1 = 0
cont2 = 0
maior = 0
menor = 0
# posso fazer
# cont1 = cont2 = 0
# maior = media = 0

# tambem posso fazer
# while r in 'Ss':
while r == 'S':
    num = int(input('digite um nr: '))
    r = str(input('quer continuar? ').upper().strip())
    cont1 = cont1 + num
    cont2 += 1
    media = cont1 / cont2
    if cont2 == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if r == 'N':
        print('fim')
    elif r != 'S':
        print('digite S/N')
        r = str(input('quer continuar? ').upper().strip())
print('a media dos nrs digitados e de {:.2f}'.format(media))
print(f'o maior nr foi {maior} e o menor nr foi {menor}')
