#Loop com len
"""
Utilizando o comprimento da lista, podemos fazer um loop nela 
sem precisar contar os índices;

Isso torna nosso código dinâmico, que aceita qualquer tamanho de lista;

Exemplo: 
while a < len(lista):
"""

lista = [1,2,3,4,5,6]
i = 0

while i < len(lista):
    print (lista[i])
    i = i + 1

