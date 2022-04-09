"""
Crie um programa que receba a categoria, em um valor númerico
de um produto;
Se for 1: exiba que é uma bolsa;
Se for 2: exiba que é um tênis;
Se for 3 exiba que é uma mochila;
Caso não seja nenhum desses valores, exiba que a categoria 
não foi encontrada;
"""

categoria = int(input("Qual a categoria de seu produto "))

if categoria == 1:
    print ("Seu poduto é uma bolsa.")

elif categoria == 2:
    print ("Seu poduto é uma tênis.")

elif categoria == 3:
    print ("Seu poduto é uma mochila.")

else:
    print("Categoria não encontrada")

