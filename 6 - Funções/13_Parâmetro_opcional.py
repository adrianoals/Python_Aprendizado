#Parâmetro opcional
"""
As funções podem ser criadas com parâmetros opcionais, ou 
seja um valor pode já estar preenchido para um parâmetro;
Então podemos utilizar a função sem passar o valor do 
parâmetro;
O que pode ser útil em alguns casos, quando já temos valores 
padronizados;

Veja a sintaxe:

def teste(x=10):
    print(x)

"""

def imprime_nome(nome = "Matheus"):
    print("Olá %s" %nome)

imprime_nome ()
imprime_nome ("João")
imprime_nome ("Pedro")


