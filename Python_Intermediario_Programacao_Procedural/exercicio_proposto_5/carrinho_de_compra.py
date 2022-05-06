carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 1', 20))
carrinho.append(('Produto 1', 50))

total = 0
for produto in carrinho:
    total += produto[1]
print(total)

#
# compra = [(y) for x, y in carrinho]
# print(sum(compra))
compra = sum([float(y) for x, y in carrinho])
print(f'O valor total da sua compra é: R$', compra)