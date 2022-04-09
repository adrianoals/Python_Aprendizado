"""
Escreve uma função que receba uma lista de números;
Calcule a média dos números da lista;
"""

def cal_media(lista):
    media = 0
    soma = 0

    for n in lista:
        soma += n

    media = soma / len(lista)

    return media 

notas = [9, 8, 7]

media_prova = cal_media(notas)
print (media_prova)

numeros = [2,3,4,5,8,9,9,]
media_numeros = cal_media(numeros)
print(media_numeros)



