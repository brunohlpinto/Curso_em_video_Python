sexo = str(input('informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('dados invalidos. informe seu sexo: [M/F] ')).strip()
print('Sexo {} digitado com sucesso'.format(sexo))
