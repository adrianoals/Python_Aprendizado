"""
Crie uma lista com lista dentro dela;
Uma ídeia seria: produtos com nome, cor e preço;
Imprima cada um dos itens das lista que estão inseridas na lista pai;

"""

lista_1 = ["camiseta", "preta", 150.00]
lista_2 = ["tenis", "azul", 200.25]
lista_3 = ["calça", "branca", 300.50]

produtos = [lista_1, lista_2, lista_3]

print(produtos)

for produto in produtos:
    print("O produto é %s a cor é %s e o preço é %.2f" % (produto[0], produto[1], produto[2]))




