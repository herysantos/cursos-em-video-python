#
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostre o comprimento da hipotenusa
#

from math import hypot

x = float(input('Say the length of opposite collared: '))
y = float(input('Say the length of adjacent collared: '))

print('The length of hipotenuse is {:.2f}'.format(hypot(x, y)))
