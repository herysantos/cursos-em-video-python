#
# Crie um programa que leia duas notas de alunos e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# < 5.0 Reprovado
# 5.1 a 6.9 Recuperação
# >= 7.0 Aprovado
#

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2

if m < 5.0:
    print('Reprovado')
elif m >= 7.0:
    print('Aprovado')
else:
    print('Recuperação')
