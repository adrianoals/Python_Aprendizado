"""
Crie uma função que retorna se um número é maior
ou menor que 10;
O número deve ser passado como parâmetro;    
"""

def ret(x):
    nun = ""
    if x > 10:
        nun = "Maior que 10"
    else:
        nun = "Menor que 10"

    return nun

numero = ret(11)

print(numero)





