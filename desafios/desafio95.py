# [95]
# Refaça o exercício 93 com suporte para vários jogadores.
#

# [93]
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dict incluindo o total de gols feitos durante o campeonato.
#

jogadores = []
jogador = {}

while True:
    jogador['nome'] = input('Informe o nome do Jogador: ')
    jogador['partidas'] = int(input('Informe a quantidade de partidas: '))

    if jogador['partidas'] > 0:
        jogador['partida'] = []

    jogador['total'] = 0
    for i in range(0, jogador['partidas']):
        gols = int(input(f'Informe a quantidade de gols na {i + 1}º partida: '))
        jogador['partida'].append(gols)
        jogador['total'] += gols

    jogadores.append(jogador.copy())
    jogador.clear()

    c = input('Quer continuar? [S/N]').upper()
    if c != 'S':
        break


print(f'{"-="*20}\n'
      f'{"Cod.":<4} {"nome":<8} {"Gols":<20} {"Total":<5}')
print(f'{"-"*40}')
for i in range(0, len(jogadores)):
    print(f'{i:<4} {jogadores[i]["nome"]:<8} {str(jogadores[i]["partida"]):<20} {jogadores[i]["total"]:<5}')
print(f'{"-"*40}')