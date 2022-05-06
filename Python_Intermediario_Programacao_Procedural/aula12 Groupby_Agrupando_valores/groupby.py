from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'D'},
    {'nome': 'Rosemary', 'nota': 'A'},
    {'nome': 'Joana', 'nota': 'C'},
    {'nome': 'João', 'nota': 'E'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'F'},
    {'nome': 'José', 'nota': 'F'},
]

# ORDENAR POR NOTA E AGRUPAR
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    # for alunos in valores_agrupados:
    #     print(alunos)
    #
    # print('\n')

    quantidade = len(list(valores_agrupados))
    print(f'{quantidade} tiraram a nota: {agrupamento}')