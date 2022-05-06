"""
For em Python
Iterando strings com FOR
função range(start=0, stop, step=1)

texto = 'Python'

for letra in texto:
    print(letra)

texto = 'Python'

for n, letra in enumerate(texto):
    print(n, letra)

for n in range(10):
    print(n)

for n in range(10, 30, 2):
    print(n)

for j in range(20, 10, -1):
    print(j)

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)
"""
texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        continue
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
print(nova_string)