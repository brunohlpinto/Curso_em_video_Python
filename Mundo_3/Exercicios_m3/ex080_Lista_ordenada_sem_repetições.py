# solucao GG
valores = list()

# pedir um valor num loop de 5
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > valores[-1]:
        valores.append(num)
        # só desta forma vai adicionar a partir do final utilizando o append
    else:
        posicao = 0
        # definir uma posicao ao meio do codigo
        while posicao < len(valores):
            # len(valores) e 5; enquanto a posicao for menor que isto continua
            if num <= valores[posicao]:
                valores.insert(posicao, num)
                break
            posicao += 1
print(valores)