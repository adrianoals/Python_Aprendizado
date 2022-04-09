"""
Escreva um programa que recebe um número;
Verifique se o número é menor que 10 se não for 
imprima uma mensagem avisando que para proseguir 
precisa ser maior que 10;
No primeiro if verifique se o número é menor que 20
e imprime a multiplicação dele por 2;
Se não imprima o número multiplicado por 20;
"""

numero = int(input("Digite um número "))

if numero > 10:
    
    if numero < 20:
        print (numero * 2)
    else:
        print (numero * 20)

else:
    print("O número precisa ser maior")
