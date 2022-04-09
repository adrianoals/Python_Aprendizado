#Instrução Break
"""
Com a instrução break podemos interoomper uma repetição;
Ela pode ser inserida após determinada condição no 
código;
O break fará que o loop seja cancelado totalmente, e o 
programa continue na próxima linha de código;
"""

numero = 0

while numero <= 10:
    print (numero)

    if numero == 5:
        break

    numero = numero + 1

print ("break")