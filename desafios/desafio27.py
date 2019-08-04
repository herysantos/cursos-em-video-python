#
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#

# fullname = input('Informe o nome completo: ')
# print(fullname.strip().split()[0], fullname.strip().split()[len(fullname.strip().split()) - 1])

# Code Clean
fullname = input('Informe o nome completo: ').strip().split()
print(fullname[0], fullname[len(fullname) - 1])
