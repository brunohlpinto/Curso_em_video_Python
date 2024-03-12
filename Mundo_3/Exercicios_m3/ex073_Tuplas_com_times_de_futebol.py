premier = ('Liverpool', 'Manchester City', 'Aston Villa', 'Arsenal', 'Tottenham',
           'West Ham', 'Manchester United', 'Brighton', 'Chelsea', 'Newcastle',
           'Wolverhampton', 'Bournemouth', 'Fulham', 'Crystal Palace', 'Nottingham Forest',
           'Brentford', 'Everton', 'Luton Town', 'Burnley', 'Sheffield United')
print('Lista de equipas: ', end='')
for equipas in premier:
    print(equipas, '| ', end='')
print(f'Os primeiros 5 classificados são: {premier[0:6]}.')
print(f'Os ultimos 4 classificados são {premier[15:20]}.')  # ou {premier[-4:]}
print(f'Os clubes por ordem alfabetica: {sorted(premier)}.')
print(f'O Manchester United está no {premier.index('Manchester United')+1}º lugar.')
