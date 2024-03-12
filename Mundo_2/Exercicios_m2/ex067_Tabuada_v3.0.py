while True:
    num = int(input('digite um nr para saber a sua tabuada: '))
    t = 0
    if num <= -1:
        break
    while t < 10:
        t += 1
        produto = num * t
        print(f'{num} x {t} = {produto}')
print('fim')
# podia ter utilizado o for, seria mais simples porque sei os limites
