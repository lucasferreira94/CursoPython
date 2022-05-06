"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da
função for divisível por 5 retorne buzz. Se o parâmetro da da função for divisível por 5 e por 3
retorne FizzBuzz, caso contrário retorne o número enviado
"""
from random import randint


def fizzbuzz(n1):

    if (n1 % 3) == 0 and (n1 % 5) == 0:
        return f'FizzBuzz {n1} é divisível por 3 e 5'
    if (n1 % 3) == 0:
        return f'Fizz {n1} é divisível por 3'
    if (n1 % 5) == 0:
        return f'Buzz {n1} é diviśivel por 5'
    return n1


for i in range(100):
    aletorio = randint(0, 100)
    print(fizzbuzz(aletorio))
