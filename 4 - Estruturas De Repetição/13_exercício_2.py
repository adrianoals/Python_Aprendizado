"""
Crie um programa que recebe o valor inteiro, que será 
considerado dinheiro;
Imprima na tela o número de cédulas entregues ao usuário;
Por exemplo:
Pediu R$ 42,00, recebeu uma 4 notas de R$ 10,00 e 2 notas de R$ 1;
As notas disponíveis são: de R$ 10 e R$ 1;
Entregue todas as notas de maior para menor;
"""

valor_do_saque = int(input("Qual valor deseja sacar "))
print("Vocé deseja sacar R$ %d,00" %valor_do_saque)

nota_10 = 0
nota_1 = 0

while valor_do_saque > 0:
    while valor_do_saque >= 10:
        nota_10 = nota_10 + 1
        valor_do_saque = valor_do_saque - 10
    while valor_do_saque >= 1:
        nota_1 = nota_1 + 1
        valor_do_saque = valor_do_saque - 1

print ("Vai receber %d notas de R$ 10,00 e %d notas de R$ 1,00" %(nota_10, nota_1))

"""
Lógica do código
A repetição utiliza o valor que inserido pelo input e se caso o valor for 
subtraido por 10 ele soma a nota 10 atravéz da variável nota_10 e se o resto ou 
a sobra não for subtraido por 10 ele subtrai por um e assim a variavel 
nota_1 é somada.
Dessa forma conseguimos encontrar os valores das notas
"""