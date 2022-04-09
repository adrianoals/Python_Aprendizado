#Separando string em lista
"""
Com a função split é possível criar uma lista;
Cada item vai ser definido por um separador comum;
O separador deve ser passado como argumento;
"""

itens = "Maçaneta, Porta, Motor, Teto Solar, Janela, Embreagem"

lista = itens.split(", ")
print(lista)

teste = "Item1@Item2@Item3@Item4@"
print(teste.split("@"))

