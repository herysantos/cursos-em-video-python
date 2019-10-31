#
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para
# cada Jogo. cadastrando tudo em uma lista composta.
#
from random import randint
palpites = [[]]

c = int(input("Quantos palpites quer gerar?"))

for p in range(0, c):
    for i in range(0, 6):
        while True:
            s = randint(1, 60)
            if s not in palpites[p]:
                break
        palpites[p].append(s)
    palpites.append([])
    print(f"Segue o palpite: {palpites[p]}")

print(palpites)