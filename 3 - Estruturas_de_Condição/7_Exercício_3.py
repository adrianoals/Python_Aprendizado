"""
Escreva um programa que lê dois números;
Depois imprima o maior deles;
"""
numero_1 = int (input ("Digite um número "))
numero_2 = int (input ("Digite um número "))

print (numero_1)
print (numero_2)

if numero_1 > numero_2:
    print ("O número %d é maior que o número %d." % (numero_1, numero_2))

if numero_2 > numero_1:
    print ("O número %d é maior que o número %d." % (numero_2, numero_1))

if numero_1 == numero_2:
    print ('Os números são iguais.')





