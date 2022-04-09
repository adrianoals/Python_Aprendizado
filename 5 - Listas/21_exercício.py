"""
Crie uma lista com alguns itens;
Peça dois itens ao usuário;
identifique qual foi o item encontrado na lista
"""

itens_carro = ["Porta", "Pneu", "Estepe", "Maçaneta", "Janela", "Chave", "Motor", "Marcha"]

item_um = input("O que deseja procurar primeiro? ") 
item_dois = input("O que deseja procurar depois? ")

i = 0

while i < len(itens_carro):
    if itens_carro[i] == item_um:
        print("O primeiro objeto %s foi encontrado primeiro " %item_um)
        break
    elif itens_carro[i] == item_dois:
        print("O segundo objeto %s foi encontrado primeiro" %item_dois)
        break
i = i + 1

#Atentar nas letras maiusculas na hora de procurar






