# minha solução
""" palavras = ('CURSO'.upper(), 'VIDEO'.upper(), 'PYTHON'.upper(),
            'PROGRAMACAO'.upper(), 'EXERCICIOS'.upper())

cont = 0
for v in palavras:
    print(f'Na palavra {v} temos: ')
    for a in v:
        if a == 'A':
            print('a', end=' ')
        if a == 'E':
            print('e', end=' ')
        if a == 'I':
            print('i', end=' ')
        if a == 'O':
            print('o', end=' ')
        if a == 'U':
            print('u', end=' ')"""

# solução GG

palavras = ('curso', 'video', 'python',
            'programacao', 'exercicios')

for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    # até aqui quase igual
    for letra in p:
        if letra.lower() in 'aeiou':  # com acentuação podia ser, por exemplo: 'aeiouáéíóú'
            print(letra, end=' ')
