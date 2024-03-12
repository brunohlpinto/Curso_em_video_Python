from time import sleep
n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor valor: '))
escolha = 0
maior = 0
while not escolha == 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos nrs
    [ 5 ] sair do programa ''')
    escolha = int(input('qual a opcao?: '))
    if escolha == 1:
        soma = n1 + n2
        print('a soma entre {} e {} e de {}'.format(n1, n2, soma))
    elif escolha == 2:
        produto = n1 * n2
        print('o produto entre {} e {} e de {}'.format(n1, n2, produto))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
            print('entre {} e {} o maior nr e {}'.format(n1, n2, maior))
        elif n2 > n1:
            maior = n2
            print('entre {} e {} o maior nr e {}'.format(n1, n2, maior))
        elif n1 == n2:
            print('os dois valores sao iguais')
    elif escolha == 4:
        print('insira novos valores')
        n1 = int(input('primeiro valor: '))
        n2 = int(input('segundo valor valor: '))
    elif escolha == 5:
        print('a finalizar...')
    else:
        print('opcao invalida tente novamente')
    print('-=' * 20)
    sleep(1)
print('programa terminado')
