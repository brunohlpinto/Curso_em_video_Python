def notas(*num, situacao=False):
    """
    -> Função para analisar notas inseridas e inserilas num dicionário;
    A quantidade de notas, a maior, a menor, a média, e a situação do aluno (opcional);
    :param num: Notas digitadas
    :param situacao: Parametro para saber se quer mostrar a situação do aluno (Aprovado ou Reprovad)
    :return: Vai retornar o dicionar com as informações pretendidas
    """
    soma = maior = menor = 0
    for i, n in enumerate(num):
        soma += n
        if i == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    media = soma / len(num)
    dici_notas = {'Total': len(num), 'Maior': maior, 'Menor': menor, 'Media': media}
    if situacao:
        if media < 4.5:
            dici_notas['Situação'] = 'Reprovado'
        else:
            dici_notas['Situação'] = 'Aprovado'
    return dici_notas


valores = notas(5, 5.5, 6, situacao=True)
print(valores)
