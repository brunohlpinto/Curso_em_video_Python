todos = list()
nome_e_peso = list()
maior = menor = 0

while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    nome_e_peso.append(nome)
    nome_e_peso.append(peso)
    # podia usar um if aqui, com o len(todos) para ver maior e menor
    todos.append(nome_e_peso[:])
    nome_e_peso.clear()
    pergunta = input('Quer continuar? s/n: ').lower().strip()
    while pergunta not in 'SNsn':
        pergunta = input('Opção inválida. Quer continuar? s/n: ').lower().strip()
    if pergunta == 'n':
        break
# usar len em vez de cont!!
print(f'Foram registadas {len(todos)} pessoas.')

for p in todos:
    cont2 += 1
    if cont2 == 1:
        maior = p[1]
        menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]
        if p[1] < menor:
            menor = p[1]

print(f'O maior peso foi {maior}. Peso de {nome_pesomaior}', end='')
# for v in todos: seria mais simples
for i, v in enumerate(todos):
    if v[1] == maior:
        print(f'{v[0]}...', end='')
print(f'\nO menor peso foi {menor}. Peso de {nome_pesomenor}', end='')
for i, v in enumerate(todos):
    if v[1] == menor:
        print(f'{v[0]}...', end='')
