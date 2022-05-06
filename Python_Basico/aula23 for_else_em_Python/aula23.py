"""
For / Else em Python
"""
variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

for valor in variavel:
    if valor.lower().startswith('j'):
        print(f'Existe uma palavra que inicia com J: ""{valor}""')
else:
    print('Não existe uma palavra que comece com J')