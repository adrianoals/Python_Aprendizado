# For com listas
"""
O for funciona muito bem com listas;
Não precisamos criar um contador, pois ele percorre todos
os elementos;

Veja a sintaxe:

for x lista:
    print(x)

"""
lista = [1, 2, 3, 4, 5]

print (lista)

for n in lista:
    print("For", n)

i = 0

while i < len(lista):
    print("While", lista[i])
    i = i + 1

