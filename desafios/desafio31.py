#
# Desenvolva um programa que pergunte a distância de uma viagem em KMs.
# Calcule o preço da passagem, cobrando R$0.50 por KM para viagens até 200KM e R$0.45 para viagens mais longas
#

d = float(input('Informe a distância da viagem: '))
d = (d * 0.5) if (d <= 200) else (d * 0.45)
print('O valor total será de R$ {}'.format(d))

'''
if d <= 200.0:
    print('O valor total será de R$ {}'.format(d * 0.5))
else:
    print('O valor total será de R$ {}'.format(d * 0.45))
'''