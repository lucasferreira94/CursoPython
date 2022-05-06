nome = str(input('Qual é o seu nome? '))
idade = int(input('Qual a sua idade? '))
ano_nasc = 2021 - int(idade)

print()
print(f'{nome} tem {idade} anos. '
			f'{nome} nasceu em {ano_nasc}')