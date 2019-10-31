#
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dict incluindo o total de gols feitos durante o campeonato.
#


aproveitamento = {}
aproveitamento['total'] = 0

aproveitamento['nome'] = input('Informe o nome do Jogador: ')
aproveitamento['qntd_partidas'] = int(input('Informe a quantidade de partidas: '))

if aproveitamento['qntd_partidas'] > 0:
    aproveitamento['partida'] = []

for i in range(0, aproveitamento['qntd_partidas']):
    gols = int(input(f'Informe a quantidade de gols na {i+1}º partida: '))
    aproveitamento['partida'].append(gols)
    aproveitamento['total'] += gols

#print(f'{aproveitamento["nome"].capitalize()} teve um total de {aproveitamento["total"]} gols em {aproveitamento["qntd_partidas"]} partidas')

print(f'\n ={"-="*10 }\n ')

print(f"O Jogador {aproveitamento['nome'].capitalize()} jogou {aproveitamento['qntd_partidas']} partidas.")
for i in range(0, aproveitamento['qntd_partidas']):
    print(f"\t=> Na partida {i}, fez {aproveitamento['partida'][i]} gols.")
print(f"Foi um total de {aproveitamento['total']} gols.")