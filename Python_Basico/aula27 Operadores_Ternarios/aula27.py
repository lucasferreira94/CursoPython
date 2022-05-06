"""
Operador ternário

if logged_user:  # igual True?
    msg = 'Usuário logado'
else:
    msg = 'Usuário precisa logar'
print(msg)

--------
logged_user = True
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar'
"""
idade = input('Qual é a sua idade? ')

if not idade.isnumeric():
    print('Digite apenas números ')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'
    print(msg)