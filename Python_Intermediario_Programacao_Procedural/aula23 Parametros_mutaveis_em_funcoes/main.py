# MUTÁVEIS: Listas, Dicionários

# CÓDIGO ERRADO
"""def lista_de_clientes(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Mariana', 'Ana', 'Paulo'])

print(clientes1)
print(clientes2)"""

# CÓDIGO CORRETO
def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Mariana', 'Ana', 'Paulo'])
clientes3 = lista_de_clientes(['José', 'Zenilda'])

print(clientes1)
print(clientes2)
print(clientes3)