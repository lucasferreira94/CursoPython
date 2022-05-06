"""
Desempacotamento de Listas em Python
"""
        # n1      # n2    # n3
lista = ['Luiz', 'João', 'Maria', 1,2,3,4,5,6,7,8,9]

n1, n2, n3, *outra_lista, ultimo_da_lista = lista

print(f'Desempacotando n1: {n1}')
print(f'Desempacotando n2: {n2}')
print(f'Desempacotando n3: {n3}')
print(f'Desempacotando demais itens: {outra_lista}')
print(f'Desempacotando ultimo item: {ultimo_da_lista}')
