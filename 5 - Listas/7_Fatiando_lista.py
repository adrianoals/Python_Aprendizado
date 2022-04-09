#Fatiando Lista
"""
Semelhantes as strings, podemos resgatar só determinados 
elementos com decomposição por índice;

Precisamos passar o índice inicial e final para o Python,
e teremos uma nova lista com os elementos selecionados;

Exemplo:
lista_nova = lista[3:6]
"""
#Lógica da decomposição
"""
[:] Pega todos elementos da lista;

O primeiro elemento sempre de uma lista é o zero 
então se quiser pegar desde do primeiro elemento
utilizar o zero no valor da esquerda [0:] ou [:];

O número da direita é sempre menos -1 exemplo:
lista =[1,2,3]
Essa lista possui 3 elementos "0,1,2"
Se voce quiser pegar imprimir tudo a sintaxe
deve ser [:] ou [0:3]

"""

lista = [1, 2, 3, 4, 5, 6]

nova_lista = lista[2:5]

print (nova_lista)

n_lista = lista[2:]

print (n_lista)

i = lista[:3]

print(i)

