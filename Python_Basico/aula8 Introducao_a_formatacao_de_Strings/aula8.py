"""
*  Criar variáveis para nome (str), idade (int),
*  altura (float) e peso (float) de uma pessoa
*  criar variável com o ano atual (int)
*  obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*  obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
*  exibir um texto com todos as valores na tela usando o F-Strings (com as chaves)
"""

nome = 'Lucas'
idade = 27
altura = 1.80
peso = 75.0
ano_atual = 2021
ano_nasc = ano_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos e {altura} de altura e pesa {peso}kg.', sep='\n')
print(f'O IMC de {nome} é {imc:.2f}', sep='\n')
print(f'{nome} nasceu em {ano_nasc}.')
