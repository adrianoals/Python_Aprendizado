"""
Crie um programa que busca por um elemento;
O método de loop precisa ser "For";
Imprima a mensagem com o elemento encontrado;

"""

lista = [1, 2, 3, 4, 5]

busca_numero = int(input("Busque um número "))

encontrado = False

for n in lista:
    if n == busca_numero:
        print ("O número encontrado é %d " % n)
        print ("O número encontrado é", n)
        print ("O número {} foi encontrado" .format(n))
        encontrado = True

if encontrado == False:
    print ("Número não encontrado")

    