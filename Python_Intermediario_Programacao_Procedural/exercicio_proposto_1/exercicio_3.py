"""
3 - Crie uma função que receba 2 números. O primerio é um valor e o segundo um percentual
(ex. 10%). Retorno (return) o valor do primeiro número somado do aumento do percentual do mesmo
"""

def perc(n1, n2):
    var = n1 + (n1 * (n2/100))
    return var

num_1 = int(input('Digite o valor base: '))
num_2 = int(input('Digite o aumento percentual: '))

calc = perc(num_1, num_2)
print(f'{calc}%')