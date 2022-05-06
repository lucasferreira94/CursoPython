"""
LIST COMPREHENSION - OTIMIZAR A PERFORMANCE DO CÓDIGO; SIMPLIFICAR O CÓDIGO; E DEIXAR MAIS LIMPO
"""
# A LISTA 2 TERÁ OS VALORES DE L1 MULTIPLICADOS POR 2
l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [v * 2 for v in l1]
# print(ex1)

# PARA CADA ELEMENTO DA LISTA, CRIAR UMA TUPLA COM COORDENADAS
l2 = [2,6,9,1,3,5,4,0,8]
ex2 = [(v, v2) for v in l2 for v2 in range(3)]
# print(ex2)

l3 = ['Luiz', 'Mauro', 'Maria']
ex3 = [v.replace('a', '@').replace('i', '1') for v in l3]
# print(ex3)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
ex4 = [(x, y) for x, y in tupla]
# print(ex4)
ex4 = dict(ex4)
# print(ex4['chave2'])

l4 = list(range(100))
ex5 = [v for v in l4 if v %  3 == 0 if v % 8 == 0]
# print(ex5)

# IMPRIMIR OS VALORES NÃO DIVIŚIVEIS por 3 COM UMA MENSAGEM
ex6 = [v if v % 3 == 0 else 'Não é' for v in l4]
print(ex6)