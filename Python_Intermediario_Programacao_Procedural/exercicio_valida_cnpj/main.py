import valida_cnpj

cnpj1 = '04.252.011/0001-10'

if valida_cnpj.valida(cnpj1):
    print(f'{cnpj1} é válido')
else:
    print(f'{cnpj1} é inválido')