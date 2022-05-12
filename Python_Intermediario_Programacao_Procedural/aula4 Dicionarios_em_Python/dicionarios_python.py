"""
d1 = {'chave1':'valor da chave'}
print(d1)
-----
d1 = {'chave1':'valor da chave'}
d1['nova chave'] = 'Valor da nova chave'
print(d1['chave1'])

-----

# OUTRA FORMA DE CRIAR UMA CHAVE
d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
d1['nova_chave'] = 'Valor da nova chave'
print(d1)
-----
d1 = {
    'str' : 'valor',
    123 : 'Outro Valor',
    (1,2,3,4) : 'Tupla',
}
print(   d1[(1,2,3,4)]   )

------
d1 = {
    'str' : 'valor',
    123 : 'Outro Valor',
    (1,2,3,4) : 'Tupla',
}

if d1.get('nomedachave') is not None:
    print(d1.get('nomedachave'))

print(1234)
------

d1 = {
    'str' : 'valor',
    123 : 'Outro Valor',
    (1,2,3,4) : 'Tupla',
}

#d1['str'] = 'Valor STR atualizado'
d1.update({'nova_chave':'novo_valor'})

if d1.get('nova_chave') is not None:
    print(d1.get('nova_chave'))

------
d1 = {
    'str' : 'valor',
    123 : 'Outro Valor',
    (1,2,3,4) : 'Tupla',
}
del d1['str']
print(d1)

------
print('str' in d1)  #  A CHAVE STR EXISTE NO MEU DICIONÁRIO
print('str' in d1.keys())  # A CHAVE STR EXISTE NO MEU DICIONÁRIO (OUTRA FORMA DE CHECAR)
print('valor' in d1.values())  # EXISTEM VALORES DENTRO DAS CHAVES

-----
d1 = {
    'chave1' : 'valor',
    'chave2' : 'Outro Valor',
    'chave3' : 'Tupla',
}
for k, v in d1.items():
    print(k, v)

-----
clientes = {
    'cliente1' : {
        'nome' : 'Luiz',
        'sobrenome' : 'Otávio',
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Moreira',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
----
import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otávio']}
v = copy.deepcopy(d1)

v[1] = 'Lucas'
v['d'][0] = 'Joãozinho'

print(d1)
print(v)
--------
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]

print(lista)

d1 = dict(lista)
print(f'Essa é uma lista = {lista}')
print(f'Este é um dicionário = {d1}')
"""
# d1 = {
#     1: 2,
#     2: 3,
#     4: 5,
# }
#
# d2 = {
#     'a': 'b',
#     'c': 'd',
# }
# # d1.pop(4)
# d1.update(d2)
# print(d1)

