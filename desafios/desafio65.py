#
# Escreva um programa que leia vários números e mostre a  média, o maior e o menor número.
# O programa deve perguntar se o usuário deseja continuar a cada interação
#

contador = 0
media = 0
continuar = True

n = int(input('Informe um número:'))
maior = n
menor = n
while continuar:
    media += n
    if menor < n:
        menor = n
    if maior > n:
        maior = n
    contador += 1

    pergunta = str(input('Voçe deseja continuar? (S) Sim (N) Não :')).strip().upper()[0:1]
    continuar = True if pergunta == 'S' else False

    if continuar:
        n = int(input('Informe um número:'))

print('Média {:.1f}\nMaior: {:.1f}\nMenor: {:.1f}.'.format(media/contador, maior, menor, contador))
