"""
FAÇA UM PROGRAMA QUE PEÇA AO USUÁRIO PARA DIGITAR UM NÚMERO INTEIRO,
INFORME SE ESTE NÚMERO É PAR OU ÍMPAR. CASO O USUÁRIO NÃO DIGITE UM NÚMERO
INTEIRO, INFORME QUE NÃO É UM NÚMERO INTEIRO

"""

num = input('Digite um número INTEIRO: ')

try:
    num = int(num)

    if ((num % 2) == 0):
        print(f'O número \"{num}\" é PAR')
    else:
        print(f'O número \"{num}\" é ÍMPAR')
except:
        print(f'O número \"{num}\" não é um número INTEIRO')
