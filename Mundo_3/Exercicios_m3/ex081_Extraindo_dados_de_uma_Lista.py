lista = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    p = input('Quer continuar s/n: ').strip()
    while p not in 'sn':
        p = input('Erro. Quer continuar s/n: ')
    if p == 'n':
        break

print(f'Digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(lista)
if lista.count(5) == 0:
    print('O número 5 não foi encontrado na lista')
else:
    print('O valor 5 faz parte da lista')
# if 5 in valores: ...
# mais simples