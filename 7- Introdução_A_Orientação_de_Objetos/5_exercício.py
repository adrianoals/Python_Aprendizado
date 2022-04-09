#Exercício
"""
Crie uma classe Carro com as propriedades marca, valor, número
de portas, e tanque de gasolina;
Crie um método que abasteça o tanque de gasolina;
Crie um método dirigir que remova a gasolina baseado em km
rodada;
"""

class Carro:
    def __init__(self, marca, valor, portas, tanque):
        self.marca = marca
        self.valor = valor
        self.portas = portas
        self.tanque = tanque

    def abastecer (self, litros):
        if self.tanque >= 100:
            print ("Tanque esta cheio")      #Comentário da Lógica
        else:                                #Se o tanque for menor que 100 soma o valor do tanque
            self.tanque += litros            #o self.tanque + quanto for abastecer o "litro"
            if self.tanque > 100:
                self.tanque = 100
    
    def dirigir(self, km):
        km_por_litro = 10 
        self.tanque -= (km // km_por_litro)
     
                
fusca = Carro("VW", 15000, 4, 80)

print(fusca.marca)

#Utilizando a função abastecer
fusca.abastecer(15)
print(fusca.tanque)

#utilizando função dirigir

fusca.dirigir(100)
print(fusca.tanque)

#Utilizando a função abastecer
fusca.abastecer(15)
print(fusca.tanque)
fusca.abastecer(10)







