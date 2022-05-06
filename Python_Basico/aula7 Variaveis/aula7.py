nome = 'Lucas Ferreira' #string
idade = 27  # int
altura = 1.80  # float
e_maior = idade > 27  # bool
peso = 75
imc = peso / (altura ** 2)

print(f'´{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))