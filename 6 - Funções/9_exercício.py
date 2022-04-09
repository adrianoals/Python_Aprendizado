"""
Escreve uma função que receba uma lista de números;
A função deve retornar apenas os números pares da lista;
"""

def retona_lista_par(x):
    nova_lista = []
    
    for numero in x:
        if numero % 2 == 0:
            nova_lista.append(numero)

    return nova_lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_par = retona_lista_par(lista)

print(lista_par)

lista_2 = [2,3,4,5,6,666,7,7,888,99356, 4555,2324678]

print (retona_lista_par(lista_2))