#
# Faça um programa que calcule o valor pago por um produto considerando o seu preço normal e condição de pagamento:
# - à vista: dinheiro ou cheque: 10% OFF
# - à vista: cartão: 5% OFF
# - até 2x cartão: preço normal
# - + 3x cartão: 20% de Juros
#

price = float(input('Preços das compras: R$ '))
paymentMethod = int(input('''Informe o meio de pagamento: \n( 1 ) Dinheiro ou Cheque \n( 2 ) Cartão \n:'''))

if paymentMethod == 1:
    print('À vista no dinheiro ou cheque você vai pagar apenas R$ {:.2f}'.format(price * 0.9))
elif paymentMethod == 2:
    installment = int(input('Em quantas vezes deseja pagar? '))
    if installment == 1:
        print('À vista no cartão você vai pagar apenas R$ {:.2f}'.format(price * 0.95))
    elif installment == 2:
        print('No cartão em 2x você você não paga Juros. R$ {:.2f}'.format(price))
    else:
        print('No cartão em {}x você vai paga apenas. R$ {:.2f}'.format(installment, price * 1.2))
else:
    print('Valor Inválido.')