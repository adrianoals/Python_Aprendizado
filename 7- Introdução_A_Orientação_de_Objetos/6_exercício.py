#Exercício
"""
Crie um sistema que simule um banco, a classe deve ter um método
saque, depósito, e transferência;
Propriedades nome do proprietário da conta, saldo e quais você
precisar;
Realizar saques, depósitos, tranferências entre contas;
"""

class Banco:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo 

    def deposito (self, valor):
        self.saldo += valor

    def saque (self, valor):
        self.saldo -= valor
    
    def transferencia (self, outra_conta, valor):
        self.saldo -= valor
        outra_conta.saldo += valor

conta_matheus = Banco("Matheus", 5000)
print(conta_matheus.nome)

#Depositando
conta_matheus.deposito(1000)
print(conta_matheus.saldo)

#Saque
conta_matheus.saque(3000)
print(conta_matheus.saldo)

#Transferencia
conta_maria = Banco("Maria", 100)
conta_matheus.transferencia(conta_maria, 200)
print(conta_maria.saldo)
print(conta_matheus.saldo)

