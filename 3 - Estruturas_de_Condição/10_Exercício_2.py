"""
Escreva um programa que recebe dois números:
Insira a multiplicação entre eles em uma variável;
Se for menor ou igual a 100 o resultado insira uma 
mensagem de que o número é baixo;
Se não o número é alto;  
"""

nun_1 = float(input("Digite um número "))
nun_2 = float(input("Digite um número "))

multiplicacao = nun_1 * nun_2 

print ("A multiplicação dos dois números é %.2f" % multiplicacao)

if multiplicacao <= 100:
    print("O número é baixo")

else:
    print( "O número é alto")

    