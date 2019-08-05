#
# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$ 7.00 por cada Km acima do limite de velocidade
#

v = float(input('Informe a velocidade: '))
if v > 80.0:
    print('Você foi multado! em R${}'.format((v - 80.0) * 7.0))
else:
    print('Boa viagem!')
