class Aviao:
    __asas = 2

    def __init__(self, marca):
        self.marca = marca
    
    def mostrar_asas(self):
        print("O avião tem %s asas." %self.__asas)

aviao = Aviao("Gol")
print(aviao.marca)
"""
print(aviao.__asas)  #Não consigo acessar esse atributo por estar privado
"""
aviao.mostrar_asas()

# só consegue acessar as propriedades  dentro do objeto