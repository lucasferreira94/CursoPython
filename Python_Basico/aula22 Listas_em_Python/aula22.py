"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range

lista = [1, 2, 3, 4, 'Luiz Otavio', True, 10.5]

----------------------------------
lista = ['A', 'B', 'C', 'D', 'E']
# negativo
#     -   4    3    2    1    0

print(lista[1])
----------------------------------
lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista[5])
print(lista[0:3])
print(lista[2:])
print(lista[-1])
print(lista[::-1])

-----------------------------------
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2
print(l1)
print(l2)
print(l3)

-----------------------------------
l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)
print(l2)
-----------------------------------
l2 = [4,5,6]

l2.append('b')
l2.insert(0, 'banana')
print(l2)

------------------------------------
l2 = [4,5,6]
print(l2)
l2.insert(0, 'banana')
print(l2)
l2.pop()
print(l2)
------------------------------------
#     0 1 2 3 4 5 6 7 8
l2 = [1,2,3,4,5,6,7,8,9]
print(l2)
l2.insert(0, 'Banana')
print(l2)
del(l2[0])
print(l2)
-------------------------------------
l2 = [1,2,3,4,5,6,7,8,9]
print(max(l2))  # maior valor da lista
print(min(l2))  # menor valor da lista
--------------------------------------
#  Iterando os valores na lista
l2 = ['String', True, 10, -20.5]

for elemento in l2:
    print(f'O tipo de elemento é {type(elemento)} e seu valor é {elemento}')

"""

"""
Jogo: Pedir ao usuário apenas uma letra para adivinhar a palavra secreta
Se o usuário acertar, uma mensagem com a letra palavra secreta é exibida 
Se o usuário errar, será exibido as chances restantes e como está a construção da palavra
"""
secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if not letra.isalpha():
        print('Você digitou um caractere inválido, por favor digite uma letra [a-z]', '\n')
        continue

    elif len(letra) > 1:
        print('Ahh isso não vale digite apenas uma letra.', '\n')
        continue

    digitadas.append(letra)
    if letra in secreto:
        print(f'Uhulll a letra "{letra}" existe na palavra secreta')
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO existe na palavra secreta')
        print(f'Chances restantes: {chances}', '\n')
        chances -= 1
        digitadas.pop()  # remove a letra digitada que não está presente na palavra secreta


    #  Se a letra digitada estiver contida no segredo, será exibida
    #  Se a letra digitada não estiver no segredo, será exibido um *
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print('Que legal, VOCÊ GANHOU!!!')
        break
    else:
        print(f'A palavra secreta é assim: {secreto_temporario}', '\n')







