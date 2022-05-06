"""
2 - crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao 2 executada.
Faça a funcao1 executar duas funcçoes que recebam um numero diferente de argumentos

"""

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def sauda(nome, saudacao):
    return f'{saudacao} {nome}'

executa = mestre(sauda, 'Lucas', saudacao='Bom dia!')
print(executa)
