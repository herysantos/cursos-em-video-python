
# Crie que leia o ano de nascimendo de 7 pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
print('Por favor: Informe a data de nascimento de 7 pessoas.')

datas = []
atual = date.today().year
maiores = 0

for c in range(7):
    datas.append(int(input('Informe uma data: ')))

for c in datas:
    if (atual - c) >= 18:
        maiores += 1

print('Houve um total de {} Maiores e {} Menores'.format(maiores, 7-maiores))
