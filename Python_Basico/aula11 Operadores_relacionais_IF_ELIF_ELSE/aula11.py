"""
Operadores RElacionais -
==  igual
>  maior que
>=  maior ou igual a
<   menor que
<=  menor ou igual a
!=  diferente
"""

"""
Exercício - Determinada pessoa só poderá pegar um empréstimo caso tenha mais de 18 anos
"""

nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))

# limite para pegar empréstimo
idade_menor = 20  # Jovem
idade_maior = 30  # Passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')