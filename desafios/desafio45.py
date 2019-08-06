#
# Crie um programa que faça o computador jogar Jokenpô com você
# Pedra < Papel < Tesoura < Pedra
#

from random import randint

winner = True
computer = randint(1, 3)
gamer = int(input('Vamos Jogar! Escolha (1) Pedra (2) Papel ou (3) Tesoura: '))
gamer = gamer if 0 < gamer < 4 else exit()

if computer == 1:
    if gamer == 1:
        print('Empate!')
    elif gamer == 2:
        print('Você Ganhou!')
    else:
        print('Você Perdeu!')
elif computer == 2:
    if gamer == 1:
        print('Você Perdeu!')
    elif gamer == 2:
        print('Empate!')
    else:
        print('Você Ganhou!')
else:
    if gamer == 1:
        print('Você Ganhou!')
    elif gamer == 2:
        print('Você Perdeu!')
    else:
        print('Empate!')
