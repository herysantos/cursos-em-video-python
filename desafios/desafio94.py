#
# Crie um programa que leia NOME, SEXO e IDADE de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A médias de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.
#

pessoas = []
pessoa = {}
media = 0

while True:
    pessoa['nome'] = str(input("Informe um nome:"))
    pessoa['sexo'] = str(input(f"Informe o sexo {pessoa['nome']} [M/F]:").upper())
    pessoa['idade'] = int(input(f"Informe a idade de {pessoa['nome']}: "))
    pessoas.append(pessoa.copy())
    pessoa.clear()
    c = input("Quer continuar? [S/N]").upper().strip()
    if c != 'S':
        break

# A)
print(f'\n— Número de cadastros: {len(pessoas)}')

# B)
for i in range(0, len(pessoas)):
    media += pessoas[i]['idade']
print(f'— A média do grupo é {media / len(pessoas)} anos.')

# C)
print('— As mulheres cadastradas fora: ', end='')
for i in range(0, len(pessoas)):
    if pessoas[i]['sexo'] == 'F':
        print(f'{pessoas[i]["nome"]} ', end='')

# D)
print('\n— Pessoas com idade acima da média: ', end ='')
for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] >= (media / len(pessoas)):
        print(f'{pessoas[i]["nome"]} ', end='')
print()
