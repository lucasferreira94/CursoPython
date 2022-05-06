"""
t1 = (1,2,3, 'a', 'Luiz Otávio')
print(t1)

# Iterar
# for i in t1:
#     print(i)

# Fatiar
# print(t1[3:])
-----
t1 = (1,2,3,4,5)
t2 = (6,7,8,9,0)
t3 = t1 + t2
print(t3)
-----
t1 = 1,2,'Luiz',4,5
t2 = 6,7,8,9,10
t3 = t1 + t2

# n1 = 1  n2 = 2  n3 = Luiz  *_ = 4 até 10

n1, n2, n3, *_ = t3
print(*_)
----
t1 = (1,2,'Luiz',4,5) * 20
print(t1)
"""
t1 = (1,2,3,4,5)
t1 = list(t1)
t1[1] = 3000
print(t1)
