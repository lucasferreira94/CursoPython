"""
VALIDADOR DO LUCAS

CPF = 168.995.350-09
--------------------------------------
1 * 10 = 10          #      1 * 11 = 11 <--
6 * 9 = 54           #      6 * 10 = 60
8 * 8 = 64           #      8 * 9 = 72
9 * 7 = 63           #      9 * 8 = 72
9 * 6 = 54           #      9 * 7 = 63
5 * 5 = 25           #      5 * 6 = 30
3 * 4 = 12           #      3 * 5 = 15
5 * 3 = 15           #      5 * 4 = 20
0 * 2 = 0            #      0 * 3 = 0
    SOMA = 297       # ---> 0 * 2 = 0
11 - (297 % 11) = 11 #  SOMA = 343
11 > 9 = 0           #  11 - (343 % 11) = 9
Digito 1 = 0         # Digit 2 = 9
"""

while True:
    cpf = input('Digite seu CPF: ')
    novo_cpf = cpf[:-2]
    if not cpf.isnumeric():
        print('Digite apenas números inteiros ')
        continue
    elif len(cpf) != 11:
        print(f'O CPF precisa ter 11 números, você digitou: CPF - {cpf} - {len(cpf)} números')
        continue
    elif cpf == cpf[::-1]:
        print(f'O CPF digitado não é valido pois todos os números são iguais: {cpf}')
        continue
    break

contador = 10
soma = 0

for i in range(19):  # Loop irá rodar a qtd necessária para realizar todas as multiplicações [de 10 até 2] e depois [11 até 2]
    if i > 8:
        i = i - 9
    soma = soma + int(novo_cpf[i]) * contador

    contador -= 1

    if contador < 2:
        contador = 11
        digito = 11 - (soma % 11)

        if digito > 9:
            digito = 0
        soma = 0
        novo_cpf = str(novo_cpf) + str(digito)

if cpf == novo_cpf:
    print(f'Seu CPF é válido --> {novo_cpf}')
else:
    print(f'Seu CPF não é válido --> {novo_cpf}')

