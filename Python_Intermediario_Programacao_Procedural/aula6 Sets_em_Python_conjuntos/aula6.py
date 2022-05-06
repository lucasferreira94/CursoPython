"""
add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets
Difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos
"""

# EXEMPLO DE SET COM NUMEROS - SEMELHANTE AO DICT, PORÉM TEMOS SOMENTE OS 'VALORES'
# s1 = {1,2,3,4,5,6}
# print(s1,'\n')
#
# # ITERANDO NO SETS
# print('interando sobre o set')
# for i in s1:
#     print(i)

# CRIANDO UM SET VAZIO E ADICIONANDO VALORES CONFORME A NECESSIDADE:
# s1 = set()
# s1.add(1)
# s1.add(2)
# s1.add('a')
# s1.add('b')
# s1.add((1,2,3,'Lucas'))
# print(s1, '\n')
#
# print('Removendo um valor individual do set ---> \"2"')
# s1.discard(2)
# print(s1)

# UTILIZANDO O 'UPDATE'
#       NOS SETS, O UPDATE ATUALIZA OS ELEMENTOS,
#       FAZ ITERAÇÃO SOBRE ELES,
#       NÃO EXIBE NA FORMA ORDENADA
#       NÃO EXIBE ELEMENTOS DUPLICADOS
# s1 = set()
# s1.update([1,2,3,4,5], [4,5,6,7,8])
# print(s1,'\n', '\n')
#
# l1 = [1,1,2,2,2,3,3,3,3,4,4,4,4,4,4,4, 'Lucas', 'Lucas']
# l1 = set(l1)
# l1 = list(l1)
# print(l1)
# print(f'Exibindo o ultimo valor: \"{l1[-1]}"')

# UTILIZANDO O UNION PARA UNIR 2 SETS DIFERENTES
s1 = {1,2,3,4,5,333}
s2 = {1,2,3,4,5,6,7,8}
s3 = s1 | s2
print(f'Valor dos Sets unidos: \"{s3}"', '\n')

# UTILIZANDO O INTERSECTION PARA EXIBIR O QUE ESTIVER EM AMBOS OS SETS
s4 = s1 & s2
print(f'Valor dos Sets com o intersection: \"{s4}"', '\n')

# UTILIZANDO A DIFERENÇA ENTRE OS SETS (Os elementos que estão em s1 mas não em s2)
s5 = s1 - s2
print(f'O que está presente em S1 mas nao em S2: \"{s5}"', '\n')

# UTILIZANDO A DIFERENÇA ENTRE OS SETS (Os elementos que estão em s2 mas não em s1)
s6 = s2 - s1
print(f'O que está presente em S2 mas nao em S1: \"{s6}"', '\n')

# UTILIZANDO A DIFERENÇA SIMETRICA ENTRE OS SETS (Os elementos que não são comuns nos dois SETS)
s7 = s2 ^ s1
print(f'O que NÃO é COMUM entre S1 e S2: \"{s7}"', '\n')

# COMPARANDO AS DUAS LISTAS, REALIZANDO O CASTING DELAS PARA SET, E VERIFICANDO SE AS DUAS SÃO IDÊNTICAS EM SEUS VALORES
l1 = ['Luiz', 'João', 'Maria']
l2 = ['João', 'Maria', 'Maria', 'Maria', 'Maria', 'Luiz', 'Luiz', 'Luiz', 'Luiz']
l1 = list(set(l1))
l2 = list(set(l2))
print(l1, l2)

# OUTRO EXEMPLO UTILIZANDO CONDICIONAL SEM QUE EU FAÇA O CASTING
if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 é diferente de L2')