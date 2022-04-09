#Exercício
"""
Crie uma classe Pessoa com nome e idade;
Crie uma classe de Super herói que herda as características
básicas da pessoa;
Crie poderes especiais para o super héroi;
Testes as duas classes criando novos objetos;
"""

class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
    def falar (self):
        print("Oi eu sou o %s" %self.nome)

class Superheroi(Pessoa):
    def __init__(self, nome, idade, super_poder):
        super().__init__(nome, idade)
        self.super_poder = super_poder
    def usar_poderes(self):
        print("O herói usou seu poder de %s" %self.super_poder)


clarckkent = Pessoa("Clarck Kent", 33 )
print ("A pessoa se chama %s e possui a idade de %d" %(clarckkent.nome,clarckkent.idade))  
clarckkent.falar() 


superman = Superheroi("Super Man", 33, "super força")
print(superman.super_poder)
superman.usar_poderes()
superman.falar()


