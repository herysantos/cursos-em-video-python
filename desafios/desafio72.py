#
# Crie um programa que tenha uma tupla contendo de zero a vinte por extenso, leia um número pelo teclado
# e o imprima por extenso.
#

numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Informe um número de 0 a 20: '))
    if 0 <= n <= 20:
        break
print(f'O número escolhido foi {numbers[n]}.')
