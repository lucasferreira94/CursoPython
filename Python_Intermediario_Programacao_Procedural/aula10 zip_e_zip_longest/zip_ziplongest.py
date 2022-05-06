cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Recife']
estados = ['SP', 'MG', 'BA', 'PE']

cidades_estados = zip(cidades, estados)

# EXIBINDO CADA VALOR
# for valor in cidades_estados:
#     print(valor)

# TRANSFORMANDO EM UM DICIONÁRIO E EXIBINDO OS VALORES
print(dict(cidades_estados))

print('\n')
# POR PADRÃO O ZIP CONCATENA E EXIBE OS VALORES DA MENOR LISTA
cidades_2 = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados_2 = ['SP', 'MG', 'BA']
cidades_estados_2 = zip(estados_2, cidades_2)
print('Cidades e estados da menor lista')
print(dict(cidades_estados_2))

# ZIP LONGEST --> PREENCHE OS VALORES COM "NONE" DAS CONCATENAÇÕES MESMO QUANDO AS LISTAS SÃO DE TAMANHOS DIFERENTES

from itertools import zip_longest, count
# print('\n')
# print('ZIP LONGEST:')
#
# cidades_3 = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
# estados_3 = ['SP', 'MG', 'BA']
# cidades_estados_3 = zip_longest(estados_3, cidades_3, fillvalue='Estado')
# print(list(cidades_estados_3))

print('\n')
# UTILIZANDO A FUNÇÃO ZIP() PARA IMPRIMIR UM INDICE JUNTAMENTE COM CIDADE E ESTADO
indice = count()
cidades_4 = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados_4 = ['SP', 'MG', 'BA']

cidades_estados_4 = zip(
    indice,
    estados,
    cidades
)

# for valor in cidades_estados_4:
#     print(valor)

for indice, estados_4, cidades_4 in cidades_estados_4:
    print(indice, estados_4, cidades_4)