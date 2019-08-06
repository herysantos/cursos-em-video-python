
# crie um programa que leia uma frase qualquer e diga se ela é um palindromo. deconsiderando os espaços.
# apos a sopa
# a sacada da casa
# a torre da derrota
# o lobo ama o bolo
# anotaram a data da maratona

frase = input('Informe uma frase ou palavra e vamos ver se ela é um palindromo: ').strip()
fraseLimpa = []

for c in frase:
    if c != ' ':
        fraseLimpa.append(c)
if fraseLimpa == fraseLimpa[::-1]:
    print("É palindromo.")
else:
    print("Não é palindromo.")



