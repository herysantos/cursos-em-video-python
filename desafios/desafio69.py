# Crie um programa que leia a idade e sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntas
# se o usuário quer ou não continuar. No final mostre:
# A: Quantas pessoas tem mais de 18 anos.
# B: Quantos homens foram cadastrados
# C: Quantas mulheres tem menos de 20 anos

mais18 = homens = mulhermenos20 = 0

while True:
    idade = int(input('Informe a ideda dessa pessoa: ').strip())

    while True:
        sexo = str(input('Informe o sexo dessa pessoa [M/F]: ').strip().upper()[0])
        if sexo == 'M' or sexo == 'F':
            break

    if sexo == 'M':
        homens += 1

    if idade > 18:
        mais18 += 1

    elif (idade < 20) and (sexo == 'F'):
        mulhermenos20 += 1

    denovo = str(input('Deseja continuar? [S/N]').strip().upper()[0])
    if denovo == 'N':
        break
print(f'Homens: {homens}\nMaiores: {mais18}\nMulheres novas: {mulhermenos20}')
