#Métodos Mágicos
"""
Python tem muitos métodos mágicos, um deles é o __str__;
Que serve para imprimir uma representação em string do que 
desejamos;
Podemos inserir este método __str__ em uma de nossas classes;
"""

class Pessoa:
    def __init__ (self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return ("O nome do usuário é %s sua idade é %d e sua profissão é %s" %(self.nome, self.idade, self.profissao))

matheus = Pessoa("Matheus", 29, "Programador")
print (matheus.__str__())
