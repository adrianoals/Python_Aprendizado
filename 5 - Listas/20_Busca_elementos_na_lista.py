#Buscando elementos na lista
"""
Podemos criar um loop que busca um elemento em um array;
A ídeia é: percorrer todos os índices e verificar se o 
elemento é igual ao elemento do índice;

Veja:

while condição:
    if lista[i] == elemento 
    print ("Encontrado")
"""

lista = ["Sofa", "Televisão", "Rádio", "AC", "Poltrona"]

i = 0

item_procurado = input("Digite o que deseja encontrar ")
achou = False

while i < len(lista):
    if lista[i] == item_procurado:
        print("Encontramos um %s" %lista[i])
        achou = True
    i = i + 1

if achou == False:
    print("Não encontramos o item procurado")
    



 