#
#   Crie um programa que leia um número real qualquer pelo teclado e mostre sua porção inteira
#

from math import trunc

n = float(input('Say me a float number: '))
print('The Integer number for {:.6f} is {}'.format(n, trunc(n)))
