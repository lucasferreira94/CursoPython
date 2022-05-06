"""
FORMATANDO VALORES COM MODIFICADORES

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^- Centro
"""

"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0^10}')


nome = 'Otávio Miranda'
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

nome = 'Otávio Miranda'
nome_formatado = '{n:0<20}'.format(n=nome)
print(nome_formatado)

nome = 'Otávio'
sobrenome = 'Miranda'
nome_formatado = '{0:$^30} {1:#^30}'.format(nome, sobrenome)
print(nome_formatado)
"""
nome = 'Otávio Miranda'
print(nome.lower())  # tudo minusculo
print(nome.upper())  # tudo maiusculo
print(nome.title())  # Primeiras letras maiusculas
