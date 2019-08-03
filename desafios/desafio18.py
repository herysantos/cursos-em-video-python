#
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente
#
from math import cos
from math import sin
from math import tan

n = float(input('Say a angle:'))
print(' Cos: {:.6f} \n Sen: {:.6f} \n Tan: {:.6f}.'.format(cos(n), sin(n), tan(n)))
