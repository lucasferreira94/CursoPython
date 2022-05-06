from dados import produtos, pessoas, lista

#  FILTRANDO A LISTA COM OS NÚMEROS MAIORES QUE 5
# nova_lista = filter(lambda x: x > 5, lista)
# print(list(nova_lista))
# MESMO RESULTADO DA FUNÇÃO ACIMA COM O LIST COMPREHENSION
# nova_lista2 = [x for x in lista if x > 5]
# print(nova_lista2)
# # ------

# PEGAR OS PRODUTOS QUE TEM O PREÇO MAIOR QUE 50
# LAMBDA
nova_lista = filter(lambda p: p['preco'] > 50, produtos)

# COM FUNÇÃO SEPARADA
# def filtra(produto):
#     if produto['preco'] > 50:
#         return True
# nova_lista = filter(filtra, produtos)
#
# for produto in nova_lista:
#     print(produto)
# ------

# # FILTRAR PELAS PESSOAS MAIORES DE IDADE
def filtra(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False

nova_lista = filter(filtra, pessoas)
for pessoa in nova_lista:
    print(pessoa)