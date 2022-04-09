"""
Crie uma lista com 5 elementos de forma dinâmica;
Ou seja, cada elemento deve ser inserido pelo usuário;
"""

lista = [0, 0, 0, 0, 0]

i = 0

while i < len(lista):
    numero = int(input("Digite um número "))
    lista[i] = numero
    i = i + 1

print(lista)