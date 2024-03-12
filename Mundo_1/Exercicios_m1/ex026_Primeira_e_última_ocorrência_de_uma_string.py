frase = str(input('digite uma frase: ')).lower().strip()
cores = {'fim': '\033[m',
         'x': '\033[36:107m',
         'first': '\033[7:36:107m',
         'last': '\033[37:107m'}
print('a letra "A" aparece {}{}{} vezes na frase.'.format(cores['x'], frase.lower().count('a'), cores['fim']))
print('a letra "A" aparece pela primeira vez na posição {}{}{}.'.format(cores['first'], frase.find('a')+1, cores['fim']))
print('a letra "A" aparece pela ultima vez na posicao {}{}{}'.format(cores['last'], frase.rfind('a')+1, cores['fim']))
# o rfind() permite procurar a partir do lado direito
