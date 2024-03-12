s = 0
c = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        s = s + i
        c = c + 1
print('a soma de todos os {} valores e {}'.format(c, s))
# ou
# s = 0
# c = 0
# for i in range(1, 501, 2):
#    if i % 3 == 0:
