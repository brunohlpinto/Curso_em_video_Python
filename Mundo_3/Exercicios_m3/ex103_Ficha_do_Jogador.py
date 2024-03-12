def ficha(n='', g=''):
    if n == '':
        n = '<desconhecido>'
    # if g.isnumeric()
    if not isinstance(g, int):
        g = 0
    return f'O jogador {n} fez {g} golos no campeonato.'


nome = input('Digite o nome do jogador: ').strip()
golos = input('Quantos golos marcou: ')
print(ficha(nome, golos))
# ainda assim as condições devem estar no programa principal

# Solução depois de ver gg
"""def ficha(n='', g=0):
    return f'O jogador {n} fez {g} golos no campeonato.'


nome = input('Digite o nome do jogador: ').strip()
golos = input('Quantos golos marcou: ')
if nome == '':
    nome = '<desconhecido>'
if golos.isnumeric()
    golos = int(golos)
else:
    golos = 0
print(ficha(nome, golos))"""
