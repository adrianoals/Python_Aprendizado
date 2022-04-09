#Cópia Lista sem referência 
"""
#Para copiar uma lista sem referência, podemos utilizar
uma sintaxe especial;
Parecida com a quais utilizamos para resgatar caracteres
de uma string, com intervalos de índices;
Exemplo:

lista_dois = lista_um[:]
"""

lista = ["Matheus", "João", "Pedro"]

nova_lista = lista[:]

print (lista)
print (nova_lista)

nova_lista[0] = "Josevaldo"

print (nova_lista)
print (lista)
