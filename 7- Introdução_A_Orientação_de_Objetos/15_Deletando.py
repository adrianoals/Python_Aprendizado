#Deletando Objetos
"""
Mais uma vez a instrução del é útil em Python;
Podemos deletar objetos por meio de del obj;
Após interpretada a linha de código, não podemos mais
acessar nem propriedades e nem métodos do objeto
removido;
"""

class Person:
    pass

matheus = Person()
joao = Person()

print(matheus)
print(joao)

del matheus

print(joao)

"""
print(matheus)

vai dar erro pois matheus foi deletado
"""