#Funções como Parâmetro
"""
Podemos inserir funções como parâmetros para outras funções;

Desta maneira podemos gerar mais reaproveitamento de código;

Proporcionando uma função utilizar várias outras apenas 
adicionando um argumento diferente na execução;
"""

def soma(a, b):
    return a + b

def multiplicação(a, b):
    return a * b

def operacao(a, b, f):
    resultado = f(a, b)
    return resultado

a = operacao (5, 5, soma)
print (a)

b = operacao (10, 5, multiplicação)
print(b)


