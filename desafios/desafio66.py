
#
# Crie um programa que leia vários números pelo inteiros teclado. O programa só vai parar quando o usuário digital 999
# que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando a flag)
#

n = soma = 0
while True:
    num = int(input('Informe um número (Digite 999 para sair): '))
    if num == 999:
        break
    n += 1
    soma += num
print(f'A quantidade de números foi {n} e a soma foi {soma}.')
