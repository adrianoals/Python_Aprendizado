"""
Escreva um programa que recebe um número;
Verifique se o número é menor que 10 se não for 
imprima uma mensagem avisando que para proseguir 
precisa ser maior que 10;
No primeiro if verifique se o número é menor que 20
e imprime a multiplicação dele por 2;
Se não imprima o número multiplicado por 20;
"""

numero = int (input("Digite um número "))
print ("Seu número é %d" % numero)

if numero > 10:
    print("Seu número é maior que 10")

    if numero < 20:
        mult = numero * 2
        print ("Seu número é %d x 2 = %d" % (numero, mult)) 
    
    else:
        mult = numero * 20
        print ("Seu número %d x 5 = %d" %(numero, mult))

else:
    print("Para proseguir seu número precisa ser maior que 10.")