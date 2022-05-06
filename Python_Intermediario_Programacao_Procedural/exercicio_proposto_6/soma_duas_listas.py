"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a = [10.1, 20.2, 30.3, 40.4, 50.5, 60.6, 70.7]
lista_b = [10.3, 20.2, 30.3, 40.4]
lista_zippada = zip(lista_a, lista_b)

# MÉTODO NORMAL DE RESOLUÇÃO
# lista_somada = []
#
# for x, y in lista_zippada:
#     soma = x + y
#     lista_somada.append(soma)
# print(lista_somada)

# MÉTODO POR LIST COMPREHENSION
# lista_somada = [(x + y) for x, y in lista_zippada]
# print(lista_somada)

# MÉTODO GENÉRICO SEM UTILIZAR OS RECURSOS DO PYTHON, QUE SERIA VÁLIDO PARA OUTRAS LINGUAGENS DE PROGRAMAÇÃO
lista_somada = []
for i in range(len(lista_b)):
    lista_somada.append(lista_a[i] + lista_b[i])
print(lista_somada)