"""
Crie um programa que receba a renda do usuário;
Baseado na renda que ele vai liberar um limite
para o cartão de crédito;
Se for menos que 2000, 1000 de limite;
Menos que 4000, 2000 de limite;
Menos que 6000, 3000 de limite;
Se for maior que 1000, insira uma mensagem para
falar com o gerente;
"""

renda = float(input("Qual é sua renda? "))
print ("Sua renda é de R$ %.2f " % renda)

if renda < 2000:
    limite = 1000

elif renda < 4000:
    limite = 2000

elif renda < 10000:
    limite = 3000

elif renda > 10000:
    print("Você precisa falar com o gerente.")
    limite = 3000

print("Parabéns seu cartão foi aprovado seu limite é de R$ %d" % limite)