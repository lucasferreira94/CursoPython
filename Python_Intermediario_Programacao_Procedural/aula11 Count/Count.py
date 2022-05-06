"""
count - Itertools
"""
from itertools import count

# COM PASSO = 1
# contador = count(start=5)

# COM PASSO = 2
# contador = count(start=5, step=2)
#
# for valor in contador:
#     print(valor)
#
#     if valor > 9:
#         break


# COM PASSO IVERTIDO
# contador = count(start=10, step=-1)
# for valor in contador:
#     print(valor)
#
#     if valor <= 5:
#         break

# GERAR ÍNDICES COM CONTADORES
contador = count()
lista = ['Luiz', 'João', 'Maria']
lista = zip(contador, lista)
print(list(lista))