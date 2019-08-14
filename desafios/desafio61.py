#
# Refaça o desafio 51, lendo o primeiro termo da razão de uma progressão aritimética, mostrando os 10 primeiros
# termos da progressão aritimética usando a estrutura while.
#

progressao = int(input('Informe o primeiro termo de uma Progressão aritimética: '))
razao = int(input('Informe a razão dessa progressão aritimética: '))
contador = 0

while contador < 10:
    print('{} : {}'.format(contador + 1, progressao))
    progressao += razao
    contador += 1
