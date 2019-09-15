#
# Crie um programa que tenha uma tupla com os 20 primeiros times do brasileirão.
# Mostre:
# A - Os 5 primeiros
# B - Os 4 útimos
# C - Em ordem alfabética
# D - A posição do chapecoense
#

brasil = ('flamengo', 'palmeira', 'santos', 'internacional', 'corintias', 'são paulo', 'bahia', 'grêmio', 'atlético',
          'botafogo', 'athletico-pr', 'vasco da gama', 'ceará sc', 'fortaleza', 'goiás', 'fluminense', 'cruzeiro',
          'csa', 'chapecoense', 'avaí')

print(f'Os 5 primeiros: {brasil[0:5]}.')
print(f'Os 4 últimos: {brasil[-4:]}.')
print(f'Ordem Alfabética: {sorted(brasil)}.')
print(f'Posição chapecoense: {brasil.index("chapecoense")+1}º.')
