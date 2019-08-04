#
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'SANTO'.
#

cidade = input('Informe o nome da cidade: ')

print('SANTO' == cidade.strip().split()[0].upper())
print('SANTO' in cidade.strip()[:5].upper())