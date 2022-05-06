"""
Operadores Lógicos
and >>>
    comparacao1 and comparacao2 (verdadeiro E verdadeiro) = verdadeiro
    comparacao1 and comparacao2 (verdadeiro E falso) = falso
--------------------------------------
or >>>
    comparacao1 and comparacao2 (verdadeiro OU verdadeiro) = verdadeiro
--------------------------------------
not >>>
    a = 2
    b = 3

    if not b > a:
        print('B é maior do que A')
    else:
        print('A é maior do que B')

    a = ''
    if not a: # a está vazio? não possui valor? então a mensagem será exibida
    print('Por favor, preencha o valor de A')
--------------------------------------
in >>>
    Checagem de caracteres nos valores da variável

    nome = 'Lucas'
    if 'u' in nome:
        print('Existe a letra \"U\" no seu nome')

--------------------------------------
not in
"""
usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Lucas'
senha_bd = '12345'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos')
