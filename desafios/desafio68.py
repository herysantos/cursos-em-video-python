#
# Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.
#

from random import randint

vitórias = 0

print('Vamos jogar Par ou Ímpar')

while True:
    jogador = int(input('Escolha seu número: '))
    escolha = str(input('Escolha Par ou Ímpar [P|I]: ').upper().strip()[0])
    computador = randint(0, 10)
    resultado = 'P' if ((computador + jogador) % 2) == 0 else 'I'

    if escolha == resultado:
        vitórias += 1
        print(f'Você Ganhou! vamos de novo')
    else:
        break
print(f'Você Perdeu! Mas você ganhou {vitórias} vezes.')
