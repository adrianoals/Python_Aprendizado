#Encapsulamento
"""
Encapsulamento é outro recurso da POO;
A ídeia é criar atributos privados que não podem ser alterados;
Fazemos isto em Python com o __ na frente dos métodos e variáveis;
Os atributos privados só são acessíveis por métodos do objeto;
"""
class Aviao:
    __asas = 2

    def __init__(self, marca):
        self.marca = marca
    
aviao = Aviao("Gol")
print(aviao.marca)

"""
print(aviao.__asas)  #Não consigo acessar esse atributo por estar privado
"""
