
salário = float(input('Informe o salário: '))
if salário <= 1250.00:
    print('Reajuste! seu salário agora é R$ {:.2f} (10%)'.format(salário * 1.1))
else:
    print('Reajuste! seu salário agora é R$ {:.2f} (15%)'.format(salário * 1.15))
