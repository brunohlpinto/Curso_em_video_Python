from datetime import date

pessoa = dict()
ano_atual = date.today().year

pessoa['nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = idade = ano_atual - nascimento
pessoa['cedula'] = int(input('Cédula profissional (digite 0 senão tiver): '))
if pessoa['cedula'] != 0:
    pessoa['ano_contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = int(input('Salario: $ '))
print(f'O nome tem valor {pessoa['nome']}')
print(f'A idade tem valor {idade}')
print(f'Cédula profissional tem o valor {pessoa['cedula']}')

if pessoa['cedula'] != 0:
    print(f'Ano de contratação tem o valor {pessoa['ano_contratacao']}')
    print(f'O salário tem o valor {pessoa['salario']}$')
    ano_aposentar = pessoa['ano_contratacao'] + 40
    print(f'A ano em que se irá aposentar é {ano_aposentar}')

# solucao GG
# fazer os prints com um for
# mais otimizado
""" for k, i in pessoa.items():
    print(f'O {k} tem valor {i}') """
