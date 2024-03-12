celsius = float(input('temperatura em graus Celsius: '))
fahr = (celsius * 1.8) + 32
print('a temperatura em celsius é \033[31:40m{:.0f}ºC\033[m e em fahrenheit é \033[7:31:40m{:.0f}ºF\033[m'.format(celsius, fahr))
# ou
# fahr = ((9*celsius)/5) + 32)
