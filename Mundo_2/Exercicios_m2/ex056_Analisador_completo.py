velho = 0
nova = 0
idades = 0
nomes = ''

for z in range(1, 5):
    print('{:^20}'.format('----- {} pessoa -----').format(z))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo: [ M/F ]: ')).strip()
    idades = idades + idade
    if z == 1 and sexo == 'M'.upper():  # ou sexo in 'Mm'
        # da proxima utilizar sexo in 'Mm'
        velho = idade
        nomes = nome
    if idade > velho and sexo in 'Mm':
        velho = idade
        nomes = nome
    if sexo in 'Ff' and idade < 20:
        # sexo in 'Ff'
        nova += 1
media = idades / 4
print('a media de idade do grupo e {}'.format(media))
print('o homem maios velho do grupo tem {} e seu nome e {}'.format(velho, nomes))
print('ao todo temos {} mulheres com menos de 20 anos'.format(nova))
