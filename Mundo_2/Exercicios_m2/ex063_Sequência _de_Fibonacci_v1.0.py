print('='*25)
print('sequencia de fibonacci')
print('='*25)
# 0 - 1 - 1

n = int(input('quantos termos quer ver?: '))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
cont = 3  #  porque inicia depois do t1(0) e o t2(1)

while cont < n: # enquanto o contador for inferior ao n digitado:
    t3 = t1 + t2
    cont += 1 # contador recebe mais para avancar
    t1 = t2
    t2 = t3
    # 0 - 1 - 1 - 2 - 3 - 5
    # t1  t2  t3
    # tenho que fazer avancar estes
    # 0 - 1 - 1 - 2 - 3 - 5
    #     t1  t2  t3  e assim sucessivamente
    print(f' -> {t3}', end='')
# quando o contador chegar ao valor do nr:
print(' -> fim')
