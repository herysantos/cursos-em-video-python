#
# Desenvolva um programa que leia 4 valores e guarde-os numa tupla.
# A - Quantas vezes o valor 9 aparece
# B - Qual a posição do valor 3
# C - Quais foram os números pares
#
num = ()

for i in range(0, 4):
    num = num + (int(input('Informe um Número: ')), )

print(f'O núemro 9 ocorre {num.count(9)} vezes.')

if 3 in num:
    print(f'O número 3 se encontra na {num.index(3)+1}° posição.')
else:
    print('Nenhuma ocorrência de 3 na lista.')

print('Os números pares encontrados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print('{} '.format(n), end='')
