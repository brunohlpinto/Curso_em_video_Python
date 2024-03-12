lista = list()

while True:
    nome = input('Nome: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    pergunta = input('Quer continuar? s/n: ')
    while pergunta not in 'sn':
        pergunta = input('Erro. Quer continuar s/n: ')
    if pergunta == 'n':
        break
print(f'{'No':<5}', end='')
print(f'{'Nome':<10}', end='')
print(f'{'Média':>5}')
for i, m in enumerate(lista):
    print(f'{i+1:<5}{m[0]:<10}{m[2]:>5}')
while True:
    aluno = int(input('Digite o nr do aluno que quer ver as notas? (999 para terminar): '))
    if aluno == 999:
        print('terminado')
        break
    if aluno - 1 <= len(lista) - 1:
        print(f'As notas de {lista[aluno-1][0]} foram {lista[aluno-1][1]}')
