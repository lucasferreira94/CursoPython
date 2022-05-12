"""
# ESSA EXPRESSÃO LAMBDA:
a = lambda x, y: x * y
print(f'Valor da expressão Lambda = {a(2,2)}')


# É IGUAL A:
def funcao(arg1, arg2):
    return arg1 * arg2

b = funcao(2,2)
print(f'Valor da função def = {b}')
"""
# ONDE APLICAR ESSE CONCEITO?

lista = [
    ['Produto_1', 13],
    ['Produto_2', 6],
    ['Produto_3', 7],
    ['Produto_4', 50],
    ['Produto_5', 8],
]

def func(item):
    return item[1]


# lista.sort(key=func)  # Imprimir do mais barato ao mais caro
# lista.sort(key=lambda item: item[1])
#lista.sort(key=lambda item: item[1], reverse=True)  # imprimir na ordem invertida
# print(lista)
# print(sorted(lista, key=lambda i: i[1]))

"""
# EXEMPLO 2 --> calcular o imposto de 30%
# EM UMA FUNÇÃO NORMAL:
preco = 1000

def calcular_imposto(preco):
    return preco * 0.3

print(calcular_imposto(preco))

# EM FORMATO LAMBDA
calcular_imposto2 = lambda preco: preco * 0.3  # Antes do ":" é valor que será passado ao LAMBDA. O que vier depois do ":" é a resposta
print(calcular_imposto2(preco))
"""

# EXEMPLO 3
precos = [100, 500, 10, 25]
impostos = list(map(lambda x: x*0.3, precos))
print(impostos)