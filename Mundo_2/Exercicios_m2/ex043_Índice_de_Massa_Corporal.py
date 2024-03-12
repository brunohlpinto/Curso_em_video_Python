peso = float(input('digite o seu peso: (kg) '))
altura = float(input('digite a sua altura: (m) '))
imc = peso / (altura ** 2)

# caso seja em (cm) e (m)
""" if altura > 3:
    altura = altura / 100
    imc = peso / (altura * altura) """

print('o seu imc e {:.1f}'.format(imc))

if imc < 18.5:
    print('abaixo do peso')
elif 18.5 <= imc < 25:
    print('peso ideal')
elif 25 <= imc < 30:
    print('sobrepeso')
elif 30 <= imc < 40:
    print('obesidade')
else:
    print('obesidade morbida')
