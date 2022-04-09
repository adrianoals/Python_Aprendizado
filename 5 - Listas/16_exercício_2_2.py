"""
Crie duas variáveis de lista;
Crie uma terceira lista com todos os elementos das listas anteriores;
"""

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 9, 10]

print(lista_1)
print(lista_2)

lista_c = []

i = 0 

while i < len(lista_1):
    lista_c.append(lista_1[i])
    i = i + 1

j = 0

while j < len(lista_2):
    lista_c.append(lista_2[j])
    j = j + 1

print(lista_c)