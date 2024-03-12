n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1+n2) / 2
print('tirando {:.2f} e {:.2f}, a media e de {:.1f}'.format(n1, n2, m))
if m < 5:
    print('o aluno esta reprovado')
elif 5 <= m < 7:
    print('o aluno esta em recuperacao')
elif 7 <= m <= 10:
    print('o aluno esta reprovado')
else:
    print('nrs invalidos')
