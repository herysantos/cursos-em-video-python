value = input('Digite algo:\n')

if value.isalnum():
    print('O valor é Alfanumérico!')

print('O valor {}'.format('é Numérico!' if value.isnumeric() else 'não é Numérico!'))

if value.isspace():
    print('O valor é um Espaço!')
else:
    print('O valor não é um Espaço!!')