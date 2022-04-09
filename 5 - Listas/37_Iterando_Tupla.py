#Iterando Tuplas
"""
Podemos iterar nas tuplas como nas listas com for;
Utilizamos a mesma sintaxe, o Python não faz distinção dos dois
tipos de dados;

Exemplo:

for x tupla:
    print(tupla[x])

"""

tupla = ("Matheus", "Jorge", "João")

print (tupla)

for nome in tupla:
    print (nome)

if nome == "João":
    print("Olá João")

i = 0

while i < len(tupla):
    print (tupla[i])
    i = i + 1

