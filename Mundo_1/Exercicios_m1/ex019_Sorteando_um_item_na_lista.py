from random import choice
aluno1 = str(input('nome do aluno 1: '))
aluno2 = str(input('nome do aluno 2: '))
aluno3 = str(input('nome do aluno 3: '))
aluno4 = str(input('nome do aluno 4: '))
inputs_alunos = [aluno1, aluno2, aluno3, aluno4]
escolha = choice(inputs_alunos)
cores = {'fim': '\033[m',
         'aluno': '\033[7:36:40m'}
print('o aluno escolhido é {}{}{}.'.format(cores['aluno'], escolha, cores['fim']))
