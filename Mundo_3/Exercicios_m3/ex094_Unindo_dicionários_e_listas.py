base_dados = list()
contpax = somaidade = contmulheres = 0
mulheres = list()
acimamedia = list()

while True:
    pessoa = dict()
    pessoa['nome'] = input('Nome: ')
    contpax += 1
    pessoa['sexo'] = input('Sexo m/f: ').strip().upper()
    while pessoa['sexo'] not in 'MmFf':
        pessoa['sexo'] = input('Erro! Sexo m/f: ').strip().upper()
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    media = somaidade / contpax
    if pessoa['idade'] > media:
        acimamedia.append(pessoa)
    base_dados.append(pessoa)
    opcao = input('Quer continuar? s/n: ').strip().upper()
    while opcao not in 'SsNn':
        opcao = input('Erro! Quer continuar? s/n: ').strip().lower()
    if opcao == 'N':
        break
print('='*20)

print(f'Foram cadastradas {contpax} pessoas.')
print(f'A média de idade é {media:.2f}')
print(f'As mulheres registadas são {", ".join(mulheres)}')
print(f'No total houve {len(acimamedia)} pessoas com idade acima da média.')
for p in acimamedia:
    print(f'Nome: {p['nome']}, Sexo: {p['sexo']}, Idade: {p['idade']}')
print('-- Fim --')
