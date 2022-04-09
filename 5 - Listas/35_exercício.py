"""
Crie um dicionário chamado carro com os seguintes valores:
pneu: 4,
portas: 2,
motor: 1,
janelas: 4,

Adicione a chave teto solar com valor 1;
Delete motor e janelas e imprimi o resultado de novo;

"""

carros = {
    "pneu": 4,
    "portas": 2,
    "motor": 1,
    "janelas": 4
}

print (carros)

carros ["teto solar"] = 1

print (carros)
print (carros["teto solar"])

del carros["janelas"]
del carros["motor"]

print (carros)

