
from random import randint

n = randint(0, 5)
print(n)
r = int(input("Tente advinhar um número entre 0 e 5: "))
if r == n:
    print('Você venceu!')
else:
    print('Você perdeu!')