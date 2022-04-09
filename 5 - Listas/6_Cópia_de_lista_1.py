#Cópia de lista
"""
#Tomar cuidado ao copiar uma lista
#Se atribuirmos um valor de uma a outra diretamente a segunda será uma referencia da primeira
#Replicando as alterações, ou seja, serão a mesma lista
"""

lista = [1, 2, 3]

nova_lista = []

nova_lista = lista

print (lista)
print (nova_lista)

nova_lista[0] = 1000

print(nova_lista)

print ("Lista um")

print (lista)

lista[0] = 500

print (nova_lista)
