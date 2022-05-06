"""
Desafio:

utilizar While / For para imprimir

0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
----------------
for ida, volta in enumerate(range(10, 1, -1)):
    print(ida, volta)
"""
ida = 0
volta = 10

while ida <=8:
    print(ida, volta)
    ida += 1
    volta -=1