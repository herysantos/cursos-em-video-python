# Ano bissexto. Se ano for menos que 1000 pega o ano atual.
from datetime import date

a = int(input('Informe o ano: '))
if a < 1000:
    a = date.today().year
if (a % 4) == 0 and (a % 100 != 0) or (a % 400 == 0):
    print('O ano {} é bissexto.'.format(a))
else:
    print('O ano {} não é bissexto.'.format(a))

'''por4 = ((a % 4) == 0)
por100 = ((a % 100) == 0)
por400 = ((a % 400) == 0)

if por100:
    if por400:
        print("É bissexto!")
    else:
        print("Não é bissexto")
else:
    if por4:
        print("É bissexto!")
    else:
        print("Não é bissexto")'''
