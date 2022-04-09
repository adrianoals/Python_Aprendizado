#Incrementando listas / Adicionando Elementos na lista
"""
Podemos incrementar listas utilizando a função append;
Um elemento será adicionado ao fim da lista;
Esta é uma das formas mais usadas para adicionar 
elementos a uma listas;

Exemplo:
lista.append(2)
"""

lista = [0, 1, 2, 3, 4]
lista.append(5)
print (lista)

nomes = ["Matheus", "João"]
nomes.append("Pedro")
print(nomes)

if nomes[2] != "Maria":
    nomes.append("Maria")
print(nomes)


