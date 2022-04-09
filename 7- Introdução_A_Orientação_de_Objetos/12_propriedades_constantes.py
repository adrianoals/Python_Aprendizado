#Propriedade Constantes
"""
Podemos também definir propriedades que não variam de
objeto em classe:
Ou seja, eles iniciam com um valor fixo;
Basta declarar fora de __self__ com algum valor;
"""

class Carro:

    rodas = 4

    def __init__ (self, marca):
        self.marca = marca

ferrari = Carro("Ferrari")

print(ferrari.marca)
print(ferrari.rodas)

