#
# Faça um programa que leia o ano de nasc. de um jovem e informe se ele ainda vai se alistar, deve se alistar esse ano ou se já passou dahora.
#
from datetime import date
anoAtual = date.today().year
ano = int(input('Informe seu ano de nascimento: '))
if anoAtual - ano < 18:
    print('Você vai precisar se alistar daqui a {} anos'.format(18 - (anoAtual - ano)))
elif anoAtual - ano > 18:
    print('Já passou da hora de se alistar')
else:
    print('Este é o ano que você deve se alistar')
