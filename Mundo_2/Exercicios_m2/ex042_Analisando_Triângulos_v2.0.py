s1 = int(input('digite o primeiro segmento: '))
s2 = int(input('digite o segundo segmento: '))
s3 = int(input('digite o terceiro segmento: '))

# ou pode ou nao pode formar triangulo
# so precisa de if e else
# dentro if (pode formar triangulo)
# vamos colocar ai outro bloco que dependem dos tipos de triangulo
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('os segmentos podem formar um triangulo ', end='')
    if s1 == s2 == s3:
        print('equilátero')
    elif s1 != s2 != s3 != s1:
        print('escaleno')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('isosceles')
else:
    print('os segmentos nao podem formar um triangulo')
