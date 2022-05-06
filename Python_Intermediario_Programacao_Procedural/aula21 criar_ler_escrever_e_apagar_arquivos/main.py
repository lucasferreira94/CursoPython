# https://docs.python.org/3/library/functions.html#open

"""
file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendo linhas:')
print(file.read())
print('#######')

# LEITURA LINHA A LINHA DO ARQUIVO
file.seek(0, 0)
print(file.readline(), end='')
print(file.readline())
print('#######')

# LEITURA DO ARQUIVO E EXIBIÇÃO EM FORMATO DE LISTA
file.seek(0, 0)
print(file.readlines())
print()
print('#######')

# LEITURA DAS LINHAS ATRAVÉS DE UM LAÇO FOR
file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')

file.close()
--------------

# MANEIRA MAIS PYTHONICA DE SE TRABALHAR COM ARQUIVOS
# ESCREVENDO E LENDO UM ARQUIVO 'W+'
with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())

# PARA SOMENTE LER O ARQUIVO
with open('abc.txt', 'r') as file:
    print(file.read())

# ADICIONAR COISAS NO ARQUIVO PARA FAZER APPEND
with open('abc.txt', 'a+') as file:
    file.write('Outra linha\n')
    file.seek(0)
    print(file.read())

# PARA APAGAR O ARQUIVO
import os
os.remove('abc.txt')
"""



