# solução GG

expressao = input('Digite uma expressão: ')
lista = []

for s in expressao:
    if s == '(':
        lista.append('(')
    elif s == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')

if len(lista) == 0:
    print('A sua expressão é válida')
else:
    print('A sua expressão não é válida')
