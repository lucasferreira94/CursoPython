"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles
"""

def soma(n1, n2, n3):
    var = int(n1 + n2 + n3)
    print(var)

num_1 = int(input('Digite o primeiro número da soma: '))
num_2 = int(input('Digite o segundo número da soma: '))
num_3 = int(input('Digite o terceiro número da soma: '))

soma(num_1, num_2, num_3)