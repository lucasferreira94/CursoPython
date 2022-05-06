"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome
"""
def saudacao(saud, nome):
    print(saud, nome)

msg = input('Digite a saudacao: ')
name = input('Digite seu nome: ')
saudacao(msg, name)