l = float(input('Say me how largest is the wall:'))
a = float(input('Say me how higher is the wall'))
print('Ok! your wall have the dimension {:.2f}x{:.2f} e your area is {}m²'.format(l, a, (a*l)))
print('To paint this wall you will need {:.2f} liters of paint.'.format(((a*l)/2)))
