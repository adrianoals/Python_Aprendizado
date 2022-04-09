#Expressões Lógicas
"""
Os operadores lógicos podem ser combinados em expressões lógicas;
As expressões lógicas consistem em duas comparações com um operador 
lógico entre estas;
Desta maneira resumimos o código e também  podemos criar
mais variedades de comparação:
Ex:
idade > 18 and passaporte == True
"""

idade = 18
carteiraMotorista = True

print (idade >= 18 and carteiraMotorista == True)
print ("Pode dirigir")

velocidade = 90
radar = 100
radarFuncionando = False

print (velocidade > radar and radarFuncionando == True)
print ("Não foi multado")



