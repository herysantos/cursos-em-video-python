#
# Crie uma tupla única com nomes e preços de produtos, no final mostre uma listagem de preços
# organizandos os dados de maneira tabular.
#

cont = 0
produtos = (
    'Pão', 1.0,
    'Pé de pato', 18.0,
    'Carro', 28000.99,
    'Frango', 10.0,
    'Leite', 3.50
)

print(f'{"-"*35}\n{"LISTAGEM DE PREÇOS":^30}\n{"-"*35}')

'''
# Primeira maneira
for p in produtos:
    if cont % 2 == 0:
        print(f'{p:.<20}{"R$ "}', end='')
    else:
        print(f'{p:>10.2f}')
    cont += 1
'''

# Outra maneira, Sabendo que o tamanho da lista é sempre multiplo de 2.

for p in range(0, len(produtos), 2):
    print(f'{produtos[p]:.<20}{"R$ "}{produtos[p+1]:>10.2f}')
print(f'{"-"*35}')
