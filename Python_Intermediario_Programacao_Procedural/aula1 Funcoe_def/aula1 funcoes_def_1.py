"""
Funções def em Python

Exemplo de função
def funcao():
    print('Hello World!')

funcao()
funcao()
funcao()
--------
Função com parametros

def funcao(msg):  #  <--- aqui é definido a variável ou variávies que receberão o valor
    print(msg)  #  <--- aqui informamos o que será feito com a(s) variavel(eis)

funcao('Minha mensagem exibida aqui')  #  <--- aqui será passado o valor para o parametro definido na função
--------

def saudacao(msg, nome):
    print(msg, nome)

saudacao('Olá', 'Lucas')
saudacao('Oi', 'Luiz')
saudacao('Hello', 'Maria')
--------

"""

def saudacao(msg='Olá', nome='Lucas'):
    print(msg, nome)

saudacao(nome='Zezinho', msg='tchau')