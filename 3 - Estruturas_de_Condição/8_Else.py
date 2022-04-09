#Estrutura Else
"""
O else vai apenas ocorrer quando o if não for executado;
Ou seja, podemos executar outra parte do código para uma 
situação inversa do if;

Veja a estrutura:
if condição:
    código
else:
    código
"""

saldo = 500
saque = 600

if saldo >= saque:
    print  ("Você sacou %d" % saque)

else:
    print ("Você não tem saldo para sacar R$ %d" % saque)
    print ("O valor do seu saldo é R$ %d" % saldo) 

saldo = float(input("Digite seu saldo "))
saque = float(input("Digite o valor que deseja sacar "))

if saldo >= saque:
    print  ("Você sacou %.2f" % saque)

else:
    print ("Você não tem saldo para sacar R$ %.2f" % saque)
    print ("O valor do seu saldo é R$ %.2f" % saldo) 