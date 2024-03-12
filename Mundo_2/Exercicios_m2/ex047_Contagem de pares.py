for p in range(1, 51):
    if p % 2 == 0:
        print(p, end=' ')
print('fim')
# ou
# gasta menos do processador
# mas nao diz se o nr e par
for p in range(2, 51, 2):
    print(p, end=' ')
print('fim')
