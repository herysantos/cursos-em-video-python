#
# Refaça o desafio 51, lendo o primeiro termo da razão de uma progressão aritimética, mostrando os 10 primeiros
# mostrando a quantidade de termos que o usuário informar usando a estrutura while.
#

progressao = int(input('Informe o primeiro termo de uma Progressão aritimética: '))
razao = int(input('Informe a razão dessa progressão aritimética: '))

mostrar = 1
contador_geral = 0
while mostrar != 0:
    mostrar = int(input('Quantos termos você quer mostrar? '))
    contador = 0
    while contador != mostrar:
        print('{} : {}'.format(contador_geral + 1, progressao))
        progressao += razao
        contador += 1
        contador_geral += 1
