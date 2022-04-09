"""
Crie um programa com variável salário;
Se for maior que R$ 1800,00 imprima a 
mensagem de que é necessário pagar IR;
Se não imprima a mensagem que não precisa
pagar IR;
"""

salario = float(input("Digite seu salário "))

print ("Seu salário é R$ %.2f" % salario) 

if salario >= 1800:
    print ("É necessário pagar IR.")

else:
    print ("Você não precisa pagar IR.")