"""
Split, Join, Enumerate
* Split - Dividir uma string  # str
* Join - Juntar uma lista  # str
* Enumarete - Enumerar elementos da lista  # iteráveis

--------------------
string = 'O Brasil é o país do futebol, o Brasil é penta'
lista_1 = string.split(' ')
#lista_2 = string.split(',')

for valor in lista_1:
    print(f'A palavra ""{valor}"" apareceu {lista_1.count(valor)}X na frase')
--------------------
string = 'O Brasil é o país do futebol, o Brasil é penta'
lista_1 = string.split(' ')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes é {palavra} ({contagem})X')
--------------------
string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ','.join(lista)

print(lista, '\n')
print(string2)
--------------------
string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor)

--------------------

"""
lista = [
    [0,'Luiz'],
    [1,'Joao'],
    [2,'Maria']
]

for indice, nome in lista:
    print(indice, nome)