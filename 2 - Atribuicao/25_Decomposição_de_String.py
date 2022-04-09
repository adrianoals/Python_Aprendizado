#Manipulação de uma string / decomposição
"""
Podemos resgatar uma parte da string atravéz 
dos índices dos caracteres;
Está pratica é bem útil conhecida também como 
manipulação de string;
Exemplo:
print(frase[0:5]) => Resgatando do primeiro ao quinto índice;
"""

teste = "Palavra"
print (teste[0:4])

frase = "Hoje está sol em Floripa"
print (frase[10:13])

sol = frase[10:13]

print ("Temos um dia de %s" % sol)