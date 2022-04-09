#Adicionando Métodos
"""
Métodos são funções criadas para objetos;
Que podem interagir com o próprio objeto ou outros;
A palavra reservada self se trata sempre do objeto em si;
Iniciamos os métodos com def, como funções;
"""

class Carros:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

    def ligar (self):
        print ("Vrummm")

    #   Outra possibilidade seria alterar a propriedade do carro

    def mudar_preco(self, novo_preco):
        self.preco = novo_preco


polo = Carros("VW", 60000)

print(polo.marca)
print(polo.preco)
polo.ligar()

#exemplo dois alterando a propriedade

polo.mudar_preco(90000)
print(polo.preco)


