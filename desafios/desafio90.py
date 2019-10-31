#
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final mostre o conteúdo da estrutura na tela.
#

import time
start = time.time()

aluno = {}
aluno['nome'] = str(input('Informe o nome do aluno: '))
aluno['media'] = int(input('Informe a média do aluno: '))

print(f'O aluno {aluno["nome"]} está {"aprovado!" if aluno["media"] >= 5 else "Reprovado!"}')

print(f'Tempo de execução: {time.time() - start:.5f} segundos.')
