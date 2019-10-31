#
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.
#

boletim = []
notas = []
linha = []
while True:
    nome = str(input('Nome: ')).strip()
    notas.append(float(input('Nota 1:')))
    notas.append(float(input('Nota 2:')))
    linha.append(nome)
    linha.append(notas[:])
    boletim.append(linha[:])
    notas.clear()
    linha.clear()
    c = str(input("Quer continuar? [S/N]")).strip().upper()
    if c != 'S':
        break

print(f"No. Nome Média")
for i, v in enumerate(boletim):
    print(f"{i}   {v[0]}   {(v[1][0]+ v[1][1])/2}")

while True:
    cn = int(input("Mostrar notas de qual aluno? (999 para Sair)"))
    if cn == 999:
        break
    print(f"As notas de {boletim[cn][0]} são {boletim[cn][1]}")