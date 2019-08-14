#
# Melhore o jogo do desafio 28 onde o computador vai pensar um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para
# acertar
#

from random import randint

tries = 0
win = False

while not win:
    computer = randint(0, 10)
    player = int(input('Try guess what I think: '))
    tries += 1
    if player == computer:
        win = True
print('You tried {} times until win.'.format(tries))
