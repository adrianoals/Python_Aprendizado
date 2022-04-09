#Herança
"""
Herança é um conceito de orientação de objetos;
Onde uma classe herda as propriedades e métodos de outra;
Assim seus objetos herdarão também estas características;
A classe que vai herdar deve receber como parâmetro esse pai;
"""

class Veiculo: 
    def __init__(self, rodas, marca):
        self.rodas = rodas
        self.marca = marca
    
    def ligar (self):
        print("Vruuuum")

class Carro(Veiculo):                              #Lembre sempre de chamar a class pai entre parentese
    def __init__(self, rodas, marca, teto_solar):
        super ().__init__(rodas, marca)            #E usar essa função para herdas as propriedades
        self.teto_solar = teto_solar

#Exemplo de herança 1
ferrari = Carro(4,"Ferrari", True)
print(ferrari.marca)
ferrari.ligar()
print(ferrari.teto_solar)

#Exemplo 2

class Moto(Veiculo):
    def __init__ (self, rodas, marca, protecao_lateral):
        super().__init__(rodas, marca)
        self.protecao_lateral = protecao_lateral

    def empinar(self):
        print("Empinou a moto!") 

moto = Moto(2, "Honda", True)
print(moto.marca)
moto.ligar()
moto.empinar()

