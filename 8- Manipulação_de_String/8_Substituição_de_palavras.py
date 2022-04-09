#Substituição
"""
A função ' replace ' nos permite substituir algo em uma string;
Se a ocorrência se repetir ela será substituida em todas as 
repetições;
Porém podemos colocar um parâmetro que limita as substituições;
"""

frase = "O rato roeu a roupa do rei de Roma"

print(frase.replace("rato", "leão"))

frase2 = "Vou testar o replace em duas palavras testar testar"

print(frase2.replace("testar", "trocou", 2))
