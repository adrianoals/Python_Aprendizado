# Pesquisando Palavras
"""
Podemos pesquisar palavras em uma string com Python;
O operador in é mujito interessante para isso, tornando 
fácil também a tarefa;
Temos também o operador not in, que é o inverso de in;

Veja um ex:

"teste" in frase

"""
frase = "Está é a frase que queremos achar uma palavra"

print(frase)

print("........................")    #Apenas para separ os exercícios

if "frase" in frase:
    print("Achamos a frase")
print ("frase" in frase)

print("........................")    #Apenas para separ os exercícios

if "frase" not in frase:
    print("Não encontramos a frase")
print("frase" not in frase)
