
# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio pergunte ao usuário qual valor a ser sacado (Inteiro)
# e o programa vai informar  quantas células de cada valor serão entregues.
#
# OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e 1

saque = int(input('Informe o valor que deseja sacar: '))
notas50 = 0
notas20 = 0
notas10 = 0
notas01 = 0

while True:
    if saque >= 50:
        notas50 += 1
        saque -= 50
        continue
    elif saque >= 20:
        notas20 += 1
        saque -= 20
        continue
    elif saque >= 10:
        notas10 += 1
        saque -= 10
        continue
    elif saque >= 1:
        notas01 += 1
        saque -= 1
        continue
    else:
        break
print(f'Você irá receber:\n{notas50} x R$50\n{notas20} x R$20\n{notas10} x R$10\n{notas01} x R$01')
