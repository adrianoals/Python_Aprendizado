#Busca em string
"""
Python nos dá a função find que possibilita a busca em strings;
A resposta será o índice da primeira letra de ocorrência;
Caso a palavra não seja encontrada vamos receber como resultado -1;
"""

frase = "Eu quero encontrar o tubarão"

print(frase.find("peixe"))

if frase.find("peixe") >=0:
    print("Encontrei o peixe")
else:
    print("Não há peixe na frase")


print (frase.find("tubarão"))

if frase.find("tubarão") == -1:
    print("Não há tubarão na frase")
else:
    print("Achei o tubarão")