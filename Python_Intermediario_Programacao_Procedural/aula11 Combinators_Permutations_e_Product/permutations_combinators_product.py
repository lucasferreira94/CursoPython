"""
COMBINAÇÃO --> ORDEM NÃO IMPORTA
PERMUTAÇÃO --> ORDEM IMPORTA
    AMBOS NÃO REPETEM VALORES ÚNICOS
PRODUTO --> ORDEM IMPORTA E REPETE VALORES ÚNICOS
"""

#      EXEMPLO DE COMBINAÇÃO
# from itertools import combinations
# pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']
#
# for grupo in combinations(pessoas, 2):
#     print(grupo)

#   EXEMPLO DE PERMUTAÇÃO
#from itertools import permutations
# pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']
#
# for grupo in permutations(pessoas, 2):
#     print(grupo)

# EXEMPLO DE PRODUCT
from itertools import product
pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in product(pessoas, repeat=2):
    print(grupo)