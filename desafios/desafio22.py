#
# Crei um progrma aque leio o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao t-o-d-o sem considerar os espaços
# Quantas letras tem o primeiro nome
#
fullname = input('Say me your full name: ').strip()
print(fullname.upper())
print(fullname.lower())
print(len(fullname)-fullname.count(' '))
print(len(fullname.split()[0]))