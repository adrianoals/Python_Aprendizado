#O que são funções
"""
Já utilizamos diversas fuções no Python: print, len, float, input;
A ídeia principal é criar um bloco de código reutilizável
Assim podemos chamar a função em qualquer lugar e reutilizar 
sua lógica;
O ínicio da função é feito por def, veja sua sintaxe:

def digaoi(nome):
    print("Oi %s" %nome)

"""

def digaoi(nome):
    print ("Olá %s!" %nome)

digaoi("Jorge")

digaoi("Pedro")

if 10 > 5:
    digaoi("João")

digaoi("José")

def digaola():
    print ("Olá mundo")
    print ("Hello world")

digaola()
