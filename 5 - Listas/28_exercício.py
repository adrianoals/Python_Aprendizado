#Crie um programa que verifique o menor valor de uma lista;

lista = [1, 2, 3, 4, 5]

"""
menor_valor = 999999
ou
"""
menor_valor = lista[0]

for n in lista:
    if n < menor_valor:
        menor_valor = n
    
print (menor_valor)