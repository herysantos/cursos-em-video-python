#
# Desenvolva um programa que leia o peso e a altura e calculo o IMC
# Diga se 18.5 estão abaixo do peso, 18.5 e 25 Peso ideal, 25 e 30 sobrepeso ou acima de 40 Obesidade mórbida
#
# IMC = Peso / Altura ** 2

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('IMC: {:.2f}. Abaixo do Peso Ideal.'.format(imc))
elif imc <= 25.0:
    print('IMC: {:.2f}. Peso Ideal.'.format(imc))
elif imc <= 30.0:
    print('IMC: {:.2f}. Sobrepeso.'.format(imc))
elif imc <= 40.0:
    print('IMC: {:.2f}. Obesidade.'.format(imc))
else:
    print('IMC: {:.2f}. Obesidade móbida.'.format(imc))
