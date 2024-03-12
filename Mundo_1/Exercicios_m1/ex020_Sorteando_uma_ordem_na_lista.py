from random import shuffle
n1 = str(input('nome do aluno 1: '))
n2 = str(input('nome do aluno 2: '))
n3 = str(input('nome do aluno 3: '))
n4 = str(input('nome do aluno 4: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('a ordem pela qual os alunos vao ao quadro é: ')
print('\033[37:40m', lista, '\033[m')

""" # como eu fiz
import random
n1 = str(input('nome do aluno 1: '))
n2 = str(input('nome do aluno 2: '))
n3 = str(input('nome do aluno 3: '))
n4 = str(input('nome do aluno 4: '))
nomes = [n1, n2, n3, n4]
ordem = sorted(nomes)
print('a ordem pela qual os alunos vão ao quadro é {}.'.format(ordem)) """
