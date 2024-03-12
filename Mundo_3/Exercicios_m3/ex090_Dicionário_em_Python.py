aluno = dict()

aluno['nome'] = str(input('Qual é o seu nome?: '))
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
print(f'O aluno é {aluno['nome']}')
print(f'A media é {aluno['media']}')

if aluno['media'] < 7:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'
print(f'A situacao é igual a {aluno['situacao']}')
