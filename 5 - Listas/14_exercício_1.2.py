"""
Crie uma lista com 5 elementos de forma dinâmica;
Ou seja, cada elemento deve ser inserido pelo usuário;
"""

lista = []

i = 0

while i < 5:
    elemento = input("Digite um elemento da lista ")
    lista.append(elemento)
    i = i + 1

print (lista)

