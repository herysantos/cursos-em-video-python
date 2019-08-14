#
# Faça um programa que leia o sexo de uma pessoa, mas só aceito os valores M ou F.
# Caso esteja errado peça a digitação novamente até ter o valor correto.
#

sexo = 'NA'

#while (sexo != 'M') and (sexo != 'F'):
while sexo not in 'MmFf':
    sexo = str(input('Informe o sexo da pessoa: (M) Masculino (F) Feminino')).upper().strip()[0:1]

print('O sexo informado foi: {}'.format('Feminino' if sexo == 'F' else 'Masculino'))
