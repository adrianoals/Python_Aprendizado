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

if renda < 2000:
    print("Você tem disponível R$ 1.000,00 de limite no cartão.")

elif renda < 4000:
    print("Você tem disponível R$ 2.000,00 de limite no cartão.")

elif renda < 6000:
    print("Você tem disponível R$ 3.000,00 de limite no cartão.")

elif renda > 10000:
    print("Você precisa comunicar o gerente.")
