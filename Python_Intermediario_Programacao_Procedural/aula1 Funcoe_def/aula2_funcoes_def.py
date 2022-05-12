"""
Funções def - *args  **kwargs
------
def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

func(1,2,3,4,5)
"""


# def func(*args):
#     print(args)
#
# lista = [1,2,3,4,5]
# lista2 = [10, 20, 30, 40, 50]
# func(*lista, *lista2)

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# lista = [1,2,3,4,5]
# lista2 = [10, 20, 30, 40, 50]
# func(*lista, *lista2, nome='Luiz', sobrenome='Miranda')

# def func(*args, **kwargs):
#     print(args)
#
#     nome = kwargs.get('nome')
#     print(nome)
#
# lista = [1,2,3,4,5]
# lista2 = [10, 20, 30, 40, 50]
# func(*lista, *lista2, nome='Luiz', sobrenome='Miranda')

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs['nome'], kwargs['sobrenome'])
#
# lista = [1,2,3,4,5]
# lista2 = [10, 20, 30, 40, 50]
# func(*lista, *lista2, nome='Luiz', sobrenome='Miranda')