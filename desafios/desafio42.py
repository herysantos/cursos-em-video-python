#
# Leia o comprimento de três retas e informe se elas podem formar um triangulo Equilátero Isósceles ou Escaleno
#

l1 = int(input('Informe o comprimento do primeiro lado: '))
l2 = int(input('Informe o comprimento do segundo lado: '))
l3 = int(input('Informe o comprimento do terceiro lado: '))

if (abs(l2 - l3) < l1 < l2 + l3) and (abs(l1 - l3) < l2 < l1 + l3) and (abs(l1 - l2) < l3 < l1 + l2):
    if l1 == l2 == l3:
        print('Equilátero: Todos os lados iguais.')
    elif (l1 == l2) or (l1 == l3) or (l2 == l3):
        print('Isósceles: Tem dois lados iguais.')
    else:
        print('Escaleno: Todos os lados são diferentes.')
else:
    print('Não pode formar um triângulo!')
