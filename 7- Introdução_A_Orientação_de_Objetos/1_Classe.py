# O que é uma classe?
"""
As classes são moldes de objetos;
Então vamos criar uma classe que pode originar diversos objetos;
A classe originada pela palavra class;
Podemos adicionar propriedades e métodos a uma class, que serão utilizadas
por seus objetos;
A primeira letra da classe é sempre maiúscula;
"""

class Pessoa:
    def _init_(self, nome, idade, sobrenome):
        self.nome = nome
        self.idade = idade 
        self.sobrenome = sobrenome

