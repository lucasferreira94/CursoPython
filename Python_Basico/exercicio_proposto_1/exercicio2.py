"""
FAÇA UM PROGRAMA QUE PERGUNTE AO USUÁRIO E, BASEANDO-SE NO HORÁRIO DESCRITO,
EXIBA A SAUDAÇÃO APROPRIADA.
BOM DIA 0-11, BOA TARDE 12-17 E BOA NOITE 18-23
"""
hora = input('Digite a HORA entre 0 - 23: ')

if hora.isdigit():  # checando se o valor digitado são digitos numericos
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('A HORA digitada deve estar entre 0 - 23!')
    else:
        if (hora <= 11):
            print('Bom dia')
        elif (hora <= 17):
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('Digite uma hora entre 0 - 23')