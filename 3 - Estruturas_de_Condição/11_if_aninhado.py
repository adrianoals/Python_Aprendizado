#If Aninhado
"""
Um if pode estar dentro de outro if, há essa possibilidade em
Python;
Chamamos o recurso de estruturas aninhadas;
Esse tipo de lógica nos permite criar regras ainda mais 
complexas e personalizadas para a nossa aplicação;
"""

idade = int(input ("Qual é sua idade? "))

if idade >= 18:
    print ("Você pode entrar na balada.")

    meetodo_pagamento = input("Qual forma de pagamento ? ")

    if meetodo_pagamento == "dinheiro":
        print ("Pegar fila 1")
    else: 
        print ("Pegar fila 2")
    

else:
    print("Não pode entrar na balada")

