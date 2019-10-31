#
# Crie um programa que onde o usuário digite uma expressão qualquer que use parecenteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
#

# Correta:   expressao = 'z(x(x(xxxxxx)sxxxzx)zxzxzx)'
# Incorreta: expressao = 'y)z(x)(x)(x)(y'
# Incorreta: expressao = '(xx)z(xx)z((x)x)x)'

expressao = str(input("Digite a expressão:")).strip().lower()
c = 0

for i in range(0, len(expressao)):
    if expressao[i] == '(':
        c += 1
    if expressao[i] == ')':
        c -= 1
    if c < 0:
        print("Ocorreu um erro na expressão")
        exit()
if c == 0:
    print("A ordem dos parênteses está correta!")
else:
    print("Ocorreu um erro na expressão")
