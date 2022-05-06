# OBJETO ITERÁVEL?
# lista = [0, 1, 2, 3, 4]
# print(f'Objeto é iterável?', hasattr(lista, '__iter__'))
#
# # É UM ITERADOR?
# print(f'a lista é um ITERADOR?: ', hasattr(lista, '__next__'))
#
# print('\n')
# lista2 = [5, 6, 7, 8, 9]
# lista2 = iter(lista2)
# print(next(lista2))
# print(next(lista2))
# print(next(lista2))
#
# print(hasattr(lista2, '__next__'))

import sys
import time

# lista3 = list(range(100))
# print(sys.getsizeof(lista3))  # QUANTOS BYTES A LISTA ESTÁ CONSUNIMINDO?

# FUNÇÃO PARA FAZER A ITERAÇÃO EM UM RANGE DE 0-100 ATRAVEŚ DE UM GERADOR COM O YIELD
# def gera():
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
#
# g = gera()
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# OUTRA FORMA DE CRIAR UM GERADOR
l1 = [x for x in range(1000)]
print(type(l1))
lista = (x for x in range(1000))
print(type(lista))