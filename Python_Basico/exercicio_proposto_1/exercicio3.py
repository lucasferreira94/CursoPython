"""
FAÇA UM PROGRAMA QUE PEÇA O PRIMEIRO NOME DO USUÁRIO. SE O NOME TIVER 4 LETRAS OU
MENOS, ESCREVA "SEU NOME É CURTO"; SE TIVER ENTRE 5 E 6 LETRAS, ESCREVA
"SEU NOME É NORMAL"; MAIOR QUE 6 DESCREVA "SEU NOME É MUITO GRANDE"
"""
# isalpha retorna TRUE se todos caracteres forem alfabeticos, e se existe ao menos 1

nome = input('Digite seu primeiro nome: ')

if not nome.isalpha():  # Caracteres não são alfabéticos?
    print('Digite um nome válido')
else:
    if len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) <= 6:
        print('Seu nome tem tamanho normal')
    else:
        print('Seu nome é grande')



