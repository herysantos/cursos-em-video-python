
valor = float(input('Informe o valor do imóvel: R$ '))
salario = float(input('Informe seu salário: R$ '))
anos = int(input('Em quantos anos pretende pagar? '))

# Calcule o valor da prestação mensão sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

prestacao = valor / (anos * 12)
aprovacao = 'Seu crédito foi aprovado.' if (prestacao / salario) < (0.3) else 'Seu crédito não foi aprovado.'
print('O valor da prestação será R$ {:.2f}. {}'.format(prestacao, aprovacao))
