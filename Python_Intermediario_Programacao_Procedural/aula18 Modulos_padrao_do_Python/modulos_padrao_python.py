"""
 Módulos padrão do Python
 Módulos são arquivos .py (que contém código python) e servem expandir
 as funcionalidades padrão da linguagem
 Veja todos os módulos padrão do Python em:
 https://docs.python.org/3/py-modindex.html
"""

# PARA IMPORTAR SOMENTE 1 MÓDULO, NO CASO ABAIXO O PLATFORM
#from sys import platform
#print(platform)

# PARA IMPORTAR 1 MÓDULO E DAR UM APELIDO A ELE
#from sys import platform as so
#print(so)

# CHECAR QUAL S.o OU PLATAFORMA O PYTHON ESTÁ RODANDO NESSE MOMENTO
# import sys
# print(sys.platform)

# GERAR UM NUMERO INTEIRO RANDOMICAMENTE
from random import randint, random
# print(random.randint(0,10))

for i in range(10):
    # print(random.randint(0, 10))
    print(randint(0,10), random())