#
# Crie uma tupla com várias palavras sem usar acento e mostra quais são suas vogais.
#

palavras = ('levanta', 'o', 'rabo', 'da', 'vaca', 'e', 'da', 'um', 'beijo')

for p in palavras:
    print(f' A palavra {p.upper()} tem as seguintes vogais: ', end='')
    for v in p.lower():
        if v in 'aeiou':
            # ('a', 'e', 'o', 'i', 'u'):
            print(f'{v} ', end='')
    print()

