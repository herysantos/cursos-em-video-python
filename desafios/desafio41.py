#
# Faça um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade.
#

from datetime import date
ano = int(input('Informe o ano de nascimento do atleta: '))
anoAtual = date.today().year
if (anoAtual - ano) <= 9:
    print('MIRIM')
elif (anoAtual - ano) <= 14:
    print('INFANTIL')
elif (anoAtual - ano) <= 19:
    print('JUNIOR')
elif (anoAtual - ano) <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
