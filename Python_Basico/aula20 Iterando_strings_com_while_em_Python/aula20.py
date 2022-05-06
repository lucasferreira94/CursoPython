#   índices
#   0123456789............................33

"""
frase = 'o rato roeu a roupa do rei de Roma'
tamanho_frase = len(frase)
contador = 0

while contador < 10:
    print(frase[contador], contador)
    contador += 1

frase = 'o rato roeu a roupa do rei de Roma'
tamanho_frase = len(frase)
contador = 0

while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1


frase = 'o rato roeu a roupa do rei de Roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    nova_string += frase[contador]
    print(nova_string)
    contador += 1


frase = 'o rato roeu a roupa do rei de Roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''


while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    contador += 1
print(nova_string)
"""

frase = 'o rato roeu a roupa do rei de Roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input('Qual letra deseja colocar maiúscula: ')
# Iteração  <- Iterar
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(f'\""{nova_string}\""')