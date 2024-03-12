from random import randint
from time import sleep


def maior(*num):
    maioral = 0
    print('A analisar os números...')
    for i, n in enumerate(num):
        if i == 0:
            maioral = n
        else:
            if n > maioral:
                maioral = n
        print(n, end=' ')
        sleep(0.5)
    print(f'Foram analisados {len(num)} números no total')
    print(f'O maior número foi {maioral}')


maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10))
maior(randint(1, 10))
maior()
