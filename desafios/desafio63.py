# Escreva um programa que leia um valor n qualquer e mostra os n primeiros elementos da
# Sequência de fibonati Fn = Fn-1 + Fn-2
#

termos = int(input('Informe a quantidade de termos da sequência de fibonati a ser mostrados'))
contador = 0
n1 = 0
n2 = 1
aux = 0
print(n1)
while contador < termos:
    print(n2)
    aux = n1
    n1 = n2
    n2 = aux + n1
    contador += 1
