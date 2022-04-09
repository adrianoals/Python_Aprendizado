#Removendo elementos
"""
Podemos remover elementos com a instrução " del ";
Vamos precisar também do índice do elemento a ser removido;

Veja a sintaxe:

del lista[3]

"""

lista = [ 10, 20, 30 , 40]

print (lista)

del lista[0]
print (lista)

del lista[len(lista) - 1]
print (lista)


