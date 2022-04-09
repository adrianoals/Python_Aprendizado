#Substituição de Métodos
"""
Em Python é possível substituir facilmente um método herdado;
Apenas precisamos declarar ele novamente na classe filha;
E então o método da classe filha que vale para seus objetos;
"""

class Pessoa:
    def falar (self):
        print ("Olá pessoal!!")


class Matheus(Pessoa):
   pass                 

#Exemplo 1:

matheus = Matheus()
matheus.falar()
