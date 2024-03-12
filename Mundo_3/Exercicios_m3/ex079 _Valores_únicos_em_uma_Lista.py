lista_valores = list()

while True:
    num = int(input('Digite um valor: '))
    if num in lista_valores:
        num = int(input('Esse valor já existe. Digite um valor: '))
    lista_valores.append(num)
    print('Adicionado com sucesso...')
    p = input("Quer continurar? S/N: ").upper().strip()
    while p not in 'SN':
        p = input("Quer continurar? S/N: ").upper().strip()
    if p == 'N':
        break
# ou lista_valores.sort()
print(f'A lista é : {sorted(lista_valores)}')
