#Exercício 42
"""
Crie uma lista com números de 1 a 10;
Percorra a lista com um loop;
Quando encontrar o elemento 4 remova-0;
Exiba a nova lista por print;
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i = 0

while i < len(lista):
    print (lista[i])
    i = i + 1
    
    if i == 4:
        break

del lista[3]

print (lista)

