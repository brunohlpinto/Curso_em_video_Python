print('+'*50)
print('{:^50}'.format('Lista de Preços'))
print('+'*50, end='')
# '{:<30}'.format('.'*28),
precos = ('{:.<40}'.format('\nPão'), '{:<3}'.format(' E$ '), '{:>7}'.format(f'{1:.2f}'),
          '{:.<40}'.format('\nÁgua'), '{:>3}'.format(' E$ '), '{:>7}'.format(f'{1:.2f}'),
          '{:.<40}'.format('\nFruta'), '{:>3}'.format(' E$ '), '{:>7}'.format(f'{2:.2f}'),
          '{:.<40}'.format('\nLegumes'), '{:>3}'.format(' E$ '), '{:>7}'.format(f'{3:.2f}'),
          '{:.<40}'.format('\nCarne'), '{:>3}'.format(' E$ '), '{:>7}'.format(f'{4:.2f}'),
          '{:.<40}'.format('\nOvos'), '{:>3}'.format(' E$ '), '{:>7}'.format(f'{5:.2f}'))
for l in precos:
    print(f'{l}', end='')

print()
print('+'*50)

# solução interessante do GG
# utilizar par ou impar
# impar o produto / par o preco
# for pos in range(0, len(precos)
#     if pos % 2 == 0:
#         print(precos[pos])
#      else:
#         print(precos[pos])