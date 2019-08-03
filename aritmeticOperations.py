n1 = input('Escreva um valor:\n')
n2 = input('Escreva outro valor:\n')

if n1.isnumeric() and n2.isnumeric():
    n1 = float(n1)
    n2 = float(n2)
    print('Soma {}'.format(n1 + n2))
    print('Subtração {}'.format(n1 - n2))
    print('Multiplicação {}'.format(n1 * n2))

    # Formatação de print :.3f (igual a 3 casas decimais), end='' (evita a quebra de linha)
    print('Divisão {:.2f}'.format(n1 / n2), end='')
    print(' Resto {}'.format(n1 % n2))
    # print :20 (vinte caracteres), :<20 (alinhado a direita) , :>20 (Alinhado a esquerda) , :^20 (centralizado)
    print('Divisão inteira {:^10}'.format(n1 // n2))
    print('Potência {}'.format(n1 ** n2))


