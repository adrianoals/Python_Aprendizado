"""
Crie um programa que gera um número de 1 a 3;
Peça para o usuário advinhar o o número;
E identifique se ele acertou ou não;
"""
import random

numero = random.randint(1, 3)

adivinhacao = input("Adivinhe o número sorteado de 1 a 3?  ")
adivinhacao = int(adivinhacao)

if numero == adivinhacao:
    print ("Acertou")
else:
    print ("Errou")
