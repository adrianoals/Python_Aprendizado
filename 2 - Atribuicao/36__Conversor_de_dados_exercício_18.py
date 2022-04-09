"""
Crie um programa que recebe o saldo de uma conta 
bancária com R$359,56
Depois insira a nova quantida por meio de input;
Remova um valor de R$125, referente a fatura de 
cartão de crédito;
Imprima o valor final da conta após as operações 
com string dinâmica; 
"""

saldo = 359.56
ganho = float(input("Digite seu ganho "))
fatura_cartao = 125.98

saldo_final = (saldo + ganho) - fatura_cartao

print (saldo_final)


