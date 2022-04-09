#Listas com listas
"""
É possível inserir uma lista dentro de outra lista em Python;
Primeiramente criamos as listas internas e depois podemos 
constituir uma nova lista com estes itens;

Veja:

lista_pai =[lista_a, lista_b]

"""

carro_1 = ["BMW", 5000]
carro_2 = ["Ferrari", 6000]
carro_3 = ["VW", 4500] 

carros = [carro_1, carro_2, carro_3]

print(carros)

print(carros[0][0])

print(carros[0][1])

print(carros[2][0])

for carro in carros:
    print ("A marca do carro é %s" % carro[0])



