frase = input('digite um frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
# e preciso fazer as coisas separdas
# primeiro o split, depois o join e so depois o inverso

print('o inverso de {} e {}'.format(junto, inverso))
if inverso == junto:
    print('palindrome')
else:
    print('nao e palindrome')

"""palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} e {}'.format(junto, inverso))
print(junto, inverso)"""


""" rev = ''.join(reversed(frase))
print(rev)
print('o inverso de {} e {}'.format(frase, rev))
if frase == rev:
    print('e um palindrome')
else:
    print('nao e um palindrome')"""
