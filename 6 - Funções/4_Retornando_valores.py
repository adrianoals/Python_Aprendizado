#Retornando valores
"""
As funções normalmente retornam valores, por meio da instrução
return;
O retorno pode ser inserido em uma variável e utilizado 
posteriormente no nosso software;
Sintaxe:

def função(x):
    return (x + 1)
"""

#Exemplo 1
def saudacao(nome):
    return "Olá %s" % nome
sds = saudacao("Jorge")
print(sds + ", tudo bem?")

#Exemplo 2
def soma (a, b):
    return (a + b)

s = soma(5, 7)
d = soma(10, 5)

print (s)

print (s + 10)

print (s + d)

#Exemplo 3

def profissao(nome):
    p = ""
    if nome == "Matheus":
        p = "Programador"
    else:
        p = "Não identificado"
    return p 

prof = profissao ("João")

print (prof)

prof_m = profissao("Matheus")

print (prof_m)
