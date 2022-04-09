#Sequência de Parâmetros
"""
Podemos inserir uma série de parâmetros ma hora de criar
uma função;

Se estes forem do mesmo tipo, podem ajudar a criar uma função
que pode processar diversos parâmetros, veja:

def funcao (argumentos)
for x in argumentos:
    print(x)
"""

def soma_todos(*numeros):
    soma = 0
    for nun in numeros:
        soma += nun
    return soma 

s = soma_todos(5, 4, 3, 2, 66, 5, 34)

print(s)

s2 = soma_todos(1, 2, 3)

print(s2)

