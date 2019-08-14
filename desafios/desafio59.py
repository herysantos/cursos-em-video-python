#
# Crie um programa que leia dois valores e mostre um menu na tela.
#
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair
#
# Seu programa deverá realizar a operação em cada caso.
#

n1 = float(input('Informe um valor'))
n2 = float(input('Informe outro valor'))
menu = -1

while menu != 5:
    menu = int(input('''
O que você deseja fazer com esses números?
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair   '''))
    if menu == 1:
        print('A soma dos números é {}'.format(n1 + n2))
    elif menu == 2:
        print('A multiplicação dos números é {}'.format(n1 * n2))
    elif menu == 3:
        print('O maior número é {}'.format(n1 if n1 > n2 else n2))
    elif menu == 4:
        n1 = float(input('Informe um valor'))
        n2 = float(input('Informe outro valor'))
    elif menu == 5:
        print('Good bye!!!')
    else:
        print('O valor informação não é válido, por favor informe um número entre 1 e 5')
