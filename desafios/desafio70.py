
# Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final mostre:
# A: Qual é o total gasto na compra.
# B: Quantos produtos  custam mais do que R$ 1000
# C: Qual o nome do produto mais barato.

total = 0
produtosmais1000 = 0
produtomaisbaratonome = ''
produtomaisbaratovalor = 0
cont = 0

while True:
    produtonome = str(input('Informe o nome do produto: '))
    produtovalor = float(input('Informe o preço do produto (R$) :'))
    cont += 1
    if cont == 1 or produtovalor < produtomaisbaratovalor:
        produtomaisbaratonome = produtonome
        produtomaisbaratovalor = produtovalor

    total += produtovalor

    if produtovalor > 1000.00:
        produtosmais1000 += 1

    continuar = str(input('Deseja continuar? [S/N]: ').strip().upper()[0])
    if continuar == 'N':
        break
print(f'O total foi R$ {total:0.2f}, A quantidade de produtos maior que 1000 foi {produtosmais1000} '
      f'e o nome do produto mais barato é {produtomaisbaratonome}')
