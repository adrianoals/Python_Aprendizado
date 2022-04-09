# O que são objetos?
"""
Um objeto é um filho de uma classe;
Ele poderá utilizar as propriedades e métodos que foram definidas 
na classe pai;
Após sua criação o objeto é independente da classe, podendo
alterar as propriedades isoladamente;
"""
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

matheus = Pessoa("Matheus", 29, "Programador")

print(matheus)
print(type(matheus))
print(matheus.nome)
print(matheus.idade)
print(matheus.profissao)

#Pode usar o objeto com qualque estrutura de programação que aprendemos
# Como if, while e etc...

if matheus.nome == "Matheus":
    print("Olá Matheus")

nome = matheus.nome
print(nome)

