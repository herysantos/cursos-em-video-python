#
# Crie um programa que leia vários números e pare de ler quando o usuário escrever 999, que é a condição de parada.
# No final mostre quantos números foram digitados e qual a soma entre eles;
#
n = 0
contador = 0
soma = 0

while n != 999:
    n = int(input('Informe um número: (999) Para sair'))
    if n != 999:
        contador += 1
        soma += n
print('A quantidade de números informado foi {} e a soma entre eles é {}.'.format(contador, soma))
