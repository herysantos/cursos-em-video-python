
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

primo = True

n = int(input('Informe um número e vamos ver se ele é primo: '))
for c in range(n, 0, -1):
    if n % c == 0:
        if n != c != 1:
            primo = False
print('Este número{}é primo!'.format(' 'if primo else ' não '))
