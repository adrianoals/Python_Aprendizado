#Verificando Strings
"""
Temos métodos para checar palavras de ínicio e fim de uma 
string;
O método startswith verifica se uma string começa com uma
determinada palavra;
É o método endswith verifica se uma string começa com uma
determinada palavra; 
"""

frase = "Testamos o começo da string."

print (frase.startswith("Testamos"))
print (frase.startswith("string"))

if frase.startswith("Testamos") == True:
    print ("Encontramos a palavra!")

print (frase.endswith("string."))
print (frase.endswith("Testamos"))



