from datetime import date

print('='*25)


def voto(nascimento):
    idade = date.today().year - nascimento
    if idade < 18:
        return f'Com {idade} anos: Voto negado'
    elif 18 < idade < 65:
        return f'Com {idade} anos: Voto obrigatório'
    else:
        return f'Com {idade} anos: Voto opcional'


# ano já nomeado
print(voto(2000))

# ou pedir ano input
nascimento = int(input('Em que ano nasceu?: '))
print(voto(nascimento))
