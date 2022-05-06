"""
def funcao(var):
    print(var)

variavel = funcao('Valor que eu quero')
print(variavel)
-----
def funcao(var):
    return(var)

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor')
------
PODEMOS RETORNAR QUALQUER TIPO DE VALOR NAS FUNÇÕES

def dumb():
    #return
    #return True
    #return 1
    #return 1.1
    return [1,2,3,4,5]

var = dumb()
print(var, type(var))
"""
def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(10,2)

if divide:
    print(divide)
else:
    print('Conta inválida')

