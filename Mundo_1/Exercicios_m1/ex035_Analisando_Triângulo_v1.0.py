print('\033[1:35m''-=''\033[m'*20)
print('\033[4:30:46m''ANALISE DE TRIANGULOS''\033[m')
print('\033[35m''-=''\033[m'*20)

s1 = float(input('digite o priemiro segmento: '))
s2 = float(input('digite o segundo segmento: '))
s3 = float(input('digite o terceiro segmento: '))
# tambem podia colocar um ojecto
# t = s2 + s3 < s1 and s1 + s3 < s2 and s1 + s2 < s3

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('os segmentos acima \033[1:32mpodem\033[m formar um triangulo')
else:
    print('os segmentos acima \033[1:31mnao podem\033[m formar um triangulo')
