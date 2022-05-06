"""
1 - Crie uma função1 que recebe uma função2 como parametro e retorne o valor da funcao2 executada
"""

def func1():
    var_1 = func2()
    return var_1

def func2():
    var_2 = 'valor'
    return var_2

print(func1())