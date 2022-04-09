"""
Exercício 42
Crie uma lista com números de 1 a 10;
Percorra a lista com um loop;
Quando encontrar o elemento 4 remova-0;
Exiba a nova lista por print;
"""
lista = []
i = 1

while i <= 10:
    lista.append(i)
    i = i + 1

print (lista)

j = 0

while j < len(lista):
    if lista[j] == 4:
        del lista[4]
    j = j + 1

print (lista)


