#Exercício
"""
Crie uma classe Carro com as propriedades de porta, motor,
se tem teto-solar, marca, preço;
Crie objetos preenchendo valores das propriedades;
E imprima alguma coisa no terminal;
"""
class Carro:
    def __init__(self, portas, motor, teto_solar, marca, preço):
        self.portas = portas
        self.motor = motor
        self.teto_solar = teto_solar
        self.marca = marca
        self.preço = preço

polo = Carro(4, 1.0, True, "VW", 70000)

print(polo.preço)
print(polo.marca)

ferrari = Carro(2, 3.0, True, "Ferrari", 250000)
print(ferrari.marca)



