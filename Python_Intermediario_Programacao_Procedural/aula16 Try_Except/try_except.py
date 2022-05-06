# TRATANDO ERRO COMO TIPO ESPECÍFICO
# try:
#     print(a)
# except NameError as erro:
#     print('Erro no código')

# TRATANDO EXCEÇÃO DENTRO DE UM BLOCO COM MAIS EXCEÇÕES
# try:
#     a = []
#     print(a[1])
# except NameError as erro:
#     print('Erro no código')
# except IndexError as erro:
#     print('Erro de índice')
# print('Bora continuar a execução do codigo...')

#  TRATANDO EXCEÇÃO DE ERRO COM MAIS DE UM TIPO NA MESMA LINHA
# try:
#     a = {}
#     print(a[1])
# except NameError as erro:
#     print('Erro no código')
# except (IndexError, KeyError) as erro:  #  Podemos indicar mais de um tipo de erro na mesma linha, criando uma TUPLA
#     print('Erro de chave')
# print('Bora continuar a execução do codigo...')

# TRATANDO EXCEÇÃO COM ELSE --> PARA INDICAR QUE O CÓDIGO FOI EXECUTADO CORRETAMENTE
# try:
#     a = {}
#     print(a)
# except NameError as erro:
#     print('Erro no código')
# except (IndexError, KeyError) as erro:  #  Podemos indicar mais de um tipo de erro na mesma linha, criando uma TUPLA
#     print('Erro de chave')
# else:
#     print('Seu código foi executado com sucesso', '\n')
#
# print('Bora continuar a execução do codigo...')

# UTILIZANDO O FINALLY PARA SER EXECUTADO SEMPRE, HOUVENDO ERROS OU NÃO
# UTILIZANDO O EXCEPTION PARA ERROS INESPERADOS
try:
    a = 1/0
    print(a)
except NameError as erro:
    print('Erro no código')
except (Exception) as erro:  #  Podemos indicar mais de um tipo de erro na mesma linha, criando uma TUPLA
    print('Erro INESPERADO')
else:
    print('Seu código foi executado com sucesso', '\n')
finally:
    print('finalmente')

print('Bora continuar a execução do codigo...')