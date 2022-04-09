#Verificando maior valor
"""
Podemos verificar o maior valor de uma lista facilmente com for;
Faremos um loop em uma lista, e checamos se o valor atual é 
maior que o maior valor;
Este maior valor deve ser inicializado com um valor de 0;

Veja:

maior_valor = 0 
for x in lista:
    if x> maior_valor
    maior_valor = x
"""

lista = [13, 55, 87, 12, 1, 7, 43]

maior_valor = 0

for n in lista:
    if n > maior_valor:
        maior_valor = n
    
print (maior_valor)

"""
Lógica do exercício o maior valor vai sendo substituido quando 
o número do loop for maior que o maior_valor  
"""