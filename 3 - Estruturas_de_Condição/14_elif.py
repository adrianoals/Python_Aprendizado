#Estrutura Elif
"""
A estrutura elif é a forma  que temos de escrever 
outros ifs antes do else;
Ou seja, podemos fazer mais checagens no código 
antes de retornar um else;
Obs: o else não é obrigatório, podemos ter só if e elif;
"""

nome = input ("Digite seu nome ")

if nome == "Adriano":
    print ("Vocé é um admin,=.")

elif nome == "João":
    print ("Você tem permissões administrativas.")

else:
    print("Você é um suário.")

