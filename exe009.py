n = int(input('Say a number to view your multiplication table:\n'))
print('{}'.format('-'*10))
for x in range(1, 11):
    print('{} x {} = {}'.format(n, x, n*x))
print('{}'.format('-'*10))
