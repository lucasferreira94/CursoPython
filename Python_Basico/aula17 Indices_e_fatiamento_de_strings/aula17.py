"""
Manipulando strings:

* String indices
* Fatiamento de strings [inicio:fim:passo]

# positivos  [012345678]
texto = 'Python s2'

print(texto[0])
print(texto[1])
print(texto[2])
nova_string = texto[2:6]
nova_string = texto[0:6]
nova_string = texto[7:]

----------------------------
# negativos  -[987654321]
texto = 'Python s2'

nova_string = texto[-9:-3]
print(nova_string)

* Funções built-in le, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo

https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
"""

texto = 'Python s2'

#nova_string = texto[0:6:2]
#print(nova_string)


nova_string = texto[-9:-3]
print(nova_string)