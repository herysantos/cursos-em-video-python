
#
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O progrma a deve ser interrompido caso o usuário digite um valor negativo.
#

while True:
    num = int(input('Quer ver a tabuada de qual valor?'))
    if num < 0:
        print('Saindo...')
        break
    print('{}'.format("="*20))
    for i in range(1, 11, 1):
        print(f'{num} x {i} = {num * i}')
    print('{}'.format("="*20))
