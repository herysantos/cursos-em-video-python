n = (input('Say a number:\n'))

if n.isalnum():
    print('O valor é Alfanumérico!')

print('O valor {}'.format('é Numérico!' if n.isnumeric() else 'não é Numérico!'))

if n.isspace():
    print('O valor é um Espaço!')
else:
    print('O valor não é um Espaço!!')

n = int(n)
print('The double of {} is {} \nYour triple is {}\nAnd your squad is {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2))))

