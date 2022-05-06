lista = [
    ('chave1', 2),
    ('chave2', 4),
]
d1 = {x: y*2 for x, y in lista}
print(d1)

lista2 = [
    ('chave1', 'valor1'),
    ('chave2', 'valor2'),
]
d2 = {x: y for x, y in enumerate(range(5))}
print(d2)

d3 = {f'chave{x}': x**2 for x in range(5)}
print(d3)
