lp = float(input('largura da parede: '))
ap = float(input('altura da parede: '))
ap = lp*ap
tinta = ap/2
print('a area da parede é \033[7:30:46m{} m2\033[m e vai precisar de \033[30:47m{:.2f} litros\033[m de tinta'.format(ap, tinta))
