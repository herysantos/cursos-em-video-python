#
# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra A
# Em que posição ela aparece a primeira vez
# E que posição ela aparece a última vez
#

frase = input('Escreva uma frase: ').strip().upper()

print(frase.count('A'))
print(frase.find('A'))
print(frase.rfind('A'))

ultimo = len(frase) - frase[::-1].find('A') - 1
print(ultimo)
#print(frase[ultimo])


