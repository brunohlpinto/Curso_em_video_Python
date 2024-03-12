palavras = ('biblioteca', 'emprestimo', 'livro',
            'autor', 'editora', 'ano', 'titulo')

for g in palavras:
    print(f'\nNa palavra {g} temos: ', end='')
    for l in g:
        if l in 'aeiou':
            print(l, end=' ')
