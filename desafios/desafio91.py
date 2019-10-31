#
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# No final coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número no dado.
#

from random import randint

rolagem = {}

for i in range(0, 4):
    rolagem[f'jogador{i}'] = randint(0, 6)

for k in sorted(rolagem, key=rolagem.get, reverse=True): #rolagem.items():
    print(f'{k} = {rolagem[k]}')