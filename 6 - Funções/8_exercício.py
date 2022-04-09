"""
Escreve uma função que receba uma lista de números;
A função deve retornar apenas os números pares da lista;
"""

lista = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]

def pares(x):
    
    if x % 2 == 0:
        return "Esse número é par"
    else:
        return "Esse número não é par"

print(pares(lista[1]))





