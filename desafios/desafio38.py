#
# Escreva dois número inteiros e compare-os mostrando na tela uma mensagem:
# O primeiro valor é maior // o segundo valor é maior // ou // Os dois são iguais
#

n1 = int(input('Informe um valor inteiro'))
n2 = int(input('Informe outro valor inteiro'))

if n1 > n2:
    print('O primeiro é maior')
elif n2 > n1:
    print('O Segundo é maior')
else:
    print('Os valores são iguais')
