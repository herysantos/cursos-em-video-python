import datetime
dicionario = {
    'titulo':'Start Wars',
    'ano': 1997,
    'diretor':'Gorge Lukas'
}

print(dicionario.values())
print(dicionario.keys())
for k, v in dicionario.items():
    print(f'i: {k} v: {v}')


data = 25 + 35 - (datetime.date.today().year - 2018)

print(data)

print(f'{"-="*20}\n'
      f'{"Cod.":<4} {"Nome":<8} {"Gols":<10} {"Total":<5}')
print(f'{"-"*40}')
for i in range(0, 4):
    print(f'{"Cod.":<4} {"Nome":<8} {"Gols":<10} {"Total":<5}')
print(f'{"-"*40}')