
# Condição de existência de um triângulo

l1 = int(input('Informe o comprimento do primeiro lado: '))
l2 = int(input('Informe o comprimento do segundo lado: '))
l3 = int(input('Informe o comprimento do terceiro lado: '))

if (abs(l2 - l3) < l1 < l2 + l3) and (abs(l1 - l3) < l2 < l1 + l3) and (abs(l1 - l2) < l3 < l1 + l2):
    print('Pode formar um triângulo!')
else:
    print('Não pode formar um triângulo!')
