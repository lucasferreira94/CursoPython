"""
Variáveis globais

variavel = 'valor'

def func():
    print(variavel)

def func2():
    print(variavel)

func()
func2()
-----
variavel = 'valor da variável GLOBAL'

def func():
    print(variavel)

def func2():
    global variavel
    variavel = 'valor da variavel LOCAL'
    print(variavel)


func()
func2()
print(variavel)
"""
# variavel = 'valor'
#
# def func():
#     print(variavel)
#
# def func2(arg=None):
#     arg = arg.replace('v', 'c')
#     return arg
#
# func()
# outra_variavel = func2(arg=variavel)
#
# print(outra_variavel)

# variavel = 'valor'
#
# def func():
#     outra_variavel = 'valor'
#
# def func2():
#     print(outra_variavel)
#
# func()
# func2()

