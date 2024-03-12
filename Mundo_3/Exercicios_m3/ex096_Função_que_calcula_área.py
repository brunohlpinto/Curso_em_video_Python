def area(la, c):
    a = la * c
    print(f'A área do terreno com largura {la}m e comprimento {c}m é: {a} m2')


print('{:^30}'.format('--- Calcular a área de um terreno ---'))
largura = int(input('Qual a largura do terreno? (m): '))
comprimento = int(input('Qual o comprimento do terreno? (m): '))
area(largura, comprimento)
