# # PRIMEIRA FORMA DE UTILIZAR
# import vendas.calc_preco
# preco = 49.90
# preco_com_aumento = vendas.calc_preco.aumento(preco, 15)
# print(preco_com_aumento)
#
# # SEGUNDA FORMA DE UTILIZAR
# from vendas import calc_preco
# preco = 49.90
# preco_com_aumento = calc_preco.aumento(valor=preco, porcentagem=15)
# print(preco_com_aumento)

# TERCEIRA FORMA DE UTILIZAR
from vendas.calc_preco import aumento, reducao
import vendas.formata.preco as formata  # colocamos um apelido para não sobrescrever o preco logo abaixo

preco = 49.90
preco_com_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)
preco_com_reducao = reducao(valor=preco, porcentagem=15, formata=True)
print(preco_com_reducao)
print(formata.real(50))
