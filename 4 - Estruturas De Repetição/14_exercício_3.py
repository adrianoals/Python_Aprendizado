"""
Crie um programa que recebe o valor inteiro, que será 
considerado dinheiro;
Imprima na tela o número de cédulas entregues ao usuário;
Por exemplo:
Pediu R$ 60,00, recebeu uma nota de 50 e outra de 10;
As notas disponíveis são: 100, 50, 20, 10, 1;
Entregue todas as notas de maior para menor;
"""

saque = int(input("Digite o quanto quer sacar? "))

nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_1 = 0

while saque > 0:
    while saque >= 100:
        nota_100 = nota_100 + 1
        saque = saque - 100
    while saque >= 50:
        nota_50 = nota_50 + 1
        saque = saque - 50
    while saque >= 20:
        nota_20 = nota_20 + 1
        saque = saque - 20
    while saque >= 10:
        nota_10 = nota_10 + 1
        saque = saque - 10
    while saque >= 1:
        nota_1 = nota_1 + 1
        saque = saque - 1

print("Você vai receber %d notas de 100, %d notas de 50, %d notas de 20, %d notas de 10 e %d notas de 1." % (nota_100, nota_50, nota_20, nota_10, nota_1))



