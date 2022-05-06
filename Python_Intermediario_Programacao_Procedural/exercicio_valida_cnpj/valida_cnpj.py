import re

# SUBSTITUIR TUDO QUE NÃO FOR NUMS ENTRE 0-9
def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

# NÃO ACEITAR SEQUENCIAS, Exemplo: 00000000
def sequencia_numerica(cnpj):
    sequencia = len(cnpj) * cnpj[0]
    if sequencia == cnpj:
        return True
    else:
        return False

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

# def calcula_digitos(cnpj)

def valida_cnpj(cnpj):
    validador = remover_caracteres(cnpj)
    if sequencia_numerica(validador) == True:
        print('CNPJ inválido')
        return False
    else:
        return True
