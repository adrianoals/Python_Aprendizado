#Exercício
"""
Crie uma classe Mamifero com propriedades mamíferos;
Herde os detalhes desta classe e crie novas para
Cachorro, Gato e outros que quiser;
Crie objetos destas classes que herdam Mamífero;
Exiba as propriedades na tela;
"""

class Mamifero:
    def __init__(self, mamifero, pelos):
        self.mamifero = mamifero
        self.pelos = pelos

class Cachorro(Mamifero):
    def __init__ (self, mamifero, pelos, estimação):
        super().__init__ (mamifero, pelos) 
        self.estimação = estimação

class Gato(Cachorro):
    def __init__(self, mamifero, pelos, estimação, raça):
        super().__init__(mamifero, pelos, estimação)
        self.raça = raça

bili = Cachorro("mamifero", 'peludo', "doméstico")
print ("O cachorro é %s, %s e %s." %(bili.mamifero, bili.pelos, bili.estimação))

juca = Gato("mamifero", 'peludo', "doméstico", "vira-lata")
print ("O gato é %s, %s, %s e %s." %(juca.mamifero, juca.pelos, juca.estimação, juca.raça))

