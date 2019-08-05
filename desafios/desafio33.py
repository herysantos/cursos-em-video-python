
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))

#elege um menor qualquer
menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and  n3 < n2:
    menor = n3

# Elege um maior
maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O maior é {} e o menor é {}'.format(maior, menor))

'''if n1 > n2:
    if n1 > n3:
        print('Maior: {}'.format(n1))
        if n2 < n3:
            print('Menor: {}'.format(n2))
        else:
            print('Menor: {}'.format(n3))
    else:
        print('Maior: {}'.format(n3))
        if n2 < n1:
            print('Menor: {}'.format(n2))
        else:
            print('Menor: {}'.format(n1))
else:
    if n2 > n3:
        print('Maior: {}'.format(n2))
        if n1 < n3:
            print('Menor: {}'.format(n1))
        else:
            print('Menor: {}'.format(n3))
    else:
        print('Maior: {}'.format(n3))
        if n2 < n1:
            print('Menor: {}'.format(n2))
        else:
            print('Menor: {}'.format(n1))'''
