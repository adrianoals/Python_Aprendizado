"""
Faça um programa que recebe um valor como salário;
E outro como porcentagem de aumento;
Exiba o valor total após o aumento no interpretador;
"""

salário = float(input("Digite seu salário "))
aumento = float(input("Digite a porcentagem de aumento "))

salário_final = salário + (salário * (aumento/100) )

print ("O novo salário é %.2f" % salário_final)