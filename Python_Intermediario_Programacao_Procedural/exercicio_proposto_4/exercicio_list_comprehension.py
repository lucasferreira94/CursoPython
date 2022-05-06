print('Executando com list comprehension')
string = '0123456789012345678901234567890123456789'
n = 10
list_comprehension = [string[i: i + n] for i in range(0, len(string), n)]
retorno = '.'.join(list_comprehension)
print(retorno)

print('\n')
print('Executando com o FOR sem list comprehension')
string2 = ''
contador = 0
for i in string:
    string2 += str(i)
    contador += 1
    if contador == 10:
        string2 += str('.')
        contador = 0
    continue
print(string2)



