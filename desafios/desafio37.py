#
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
#
n = int(input('Informe um número para conversão: '))
c = int(input('Escolha o tipo de conversão: (1)Binário (2)Octal (3)Hexadecimal'))

if c == 1:
    print(bin(n)[2:])
elif c == 2:
    print(oct(n)[2:])
elif c == 3:
    print(hex(n)[2:])
else:
    print('Conversão inválida!')