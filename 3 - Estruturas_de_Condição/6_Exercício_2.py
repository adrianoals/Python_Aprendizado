"""
Crie um programa que receba o número de rodas
que um veículo possui;
Se for maior que 2, imprima uma mensagem para
pagar pedágio;
Se for igual a 2, imprima uma mensagem dizendo 
que pode passar livremente;
"""

veículo = int(input("Quantas rodas seu veículo possui? "))

print(veículo) 

if veículo > 2:
    print("Vai pagar pedágio")

if veículo <= 2:
    print ("Não vai pagar pedágio")