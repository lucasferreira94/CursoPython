from dados import produtos, pessoas, lista
from functools import reduce

# soma_lista = reduce(lambda acumulador, indice: indice + acumulador, lista, 0)
# print(soma_lista)

# SOMA DE PREÇOS
soma_precos = reduce(lambda acumulador, p: p['preco'] + acumulador, produtos, 0)
print(f'A soma total dos preços é: {soma_precos}')
# MÉDIA DE PREÇO DOS PRODUTOS
print(f'A média de preço dos produtos é: {soma_precos / len(produtos)}')


# MÉDIA DE IDADES DOS CLIENTES
soma_idades = reduce(lambda acumulador, id: id['idade'] + acumulador, pessoas, 0)
print(f'A média das idades é: {soma_idades / len(pessoas)}')