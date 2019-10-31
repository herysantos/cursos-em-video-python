#
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com a idade) em uma dict.
# se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
#
import datetime


def get_year(datanasc):
    if '/' in datanasc:
        ano_nasc = datanasc.split('/')[2]
    elif '-' in datanasc:
        ano_nasc = datanasc.split('-')[2]
    else:
        exit('Formato inválido.')
    return datetime.date.today().year - int(ano_nasc)


pessoa = dict()

pessoa['nome'] = input('Informe o nome: ')
pessoa['datanasc'] = input('Informe a data de nascimento: ').strip()
pessoa['idade'] = get_year(pessoa['datanasc'])
pessoa['CTPS'] = int(input('Informe o nº da CTPS (Digite 0 se não tiver): '))

if pessoa['CTPS'] != 0:
    pessoa['contratacao'] = int(input('Informe o ano da contratação: '))
    pessoa['salario'] = float(input('Informe o salário: '))
    aposentadoria = get_year(pessoa['datanasc']) + 35 - (datetime.date.today().year - pessoa['contratacao'])
else:
    aposentadoria = 65

print(f'{pessoa["nome"].capitalize()} tem {pessoa["idade"]} anos '
      f'e irá se aposentar aos {aposentadoria} anos.')
