# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual o nome do homem mais velho.
# Quantoas mulheres têm menos de 20 anos.

print('Preciso que informe o nome, idade e sexo de quatro pessoas: ')
nomes = []
idades = []
sexos = []
for c in range(4):
    nomes.append(str(input('Informe o nome {}º pessoa: '.format(c + 1))))
    idades.append(int(input('Informe a idade {}º pessoa: '.format(c + 1))))
    sexos.append(str(input('Informe o sexo {}º pessoa (M) (F): '.format(c + 1)).strip().upper()[0:1]))

media = 0
velhinho = 0
idade_velhinho = 0
mulhermenos20 = 0

for c in range(4):
    # media do grupo
    media += idades[c]
    # homem mais velho
    if sexos[c] == 'M' and idades[c] > idade_velhinho:
        idade_velhinho = idades[c]
        velhinho = c
    # mulheres com menos de 20
    if sexos[c] == 'F' and idades[c] < 20:
        mulhermenos20 += 1
media /= 4

print('A média de idades é {:.2f}'.format(media))
print('O homem mais velho é {} e tem {} anos.'.format(nomes[velhinho], idade_velhinho))
print('E apareceu {} mulheres novas.'.format(mulhermenos20))

