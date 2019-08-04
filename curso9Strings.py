frase = 'Curso em Vídeo Python'

# Strings são listas em python
for x in frase:
    print(x, end=' ')

# Exemplo de seleção de trecho em lista
print('\n \n', frase[9:13+1])

# Selecionando trecho em lista, passo 2.
print('\n', frase[9:21:2])

# Selecionando trecho sem informar início ou fim.
print(' \n', frase[:5], frase[15:])

# Mostra tamanho da lista
print(' ', len(frase))

# Conta ocorrência de um caracter ou lista em uma lista.
print(' ', frase.count('o'))

# Encontra a posição da primeira ocorrência de um caracter ou lista em uma lista. Não encontrado retorna -1
print(' ', frase.find('deo'))

# existe trecho na lista?
print('Curso' in frase)

# Substitui trecho por outro.
print(' ', frase.replace('Python', 'Android'))

# Apresenta em mauísculo ou minusculo ou captaliza
print(' ', frase.upper())
print(' ', frase.lower().capitalize())

print(' Aprendendo Pyton   '.strip())

print(frase.split())
print('/\/\\'.join(frase.split()))

# Utilizando strings em várias linhas

print("""
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard 
dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen 
book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially 
unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
""")

print("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
