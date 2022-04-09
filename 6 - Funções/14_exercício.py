"""
Escreva uma função que desenha uma escada no terminal;
Os números de degraus deve ser informado por parâmetro;
Ex:
#
##
###
####
#####
"""

def criar_escada(degraus):
    i = 1
    while i <= degraus:
        print ("#" * i)
        i = i + 1

criar_escada(3)

criar_escada(10)


