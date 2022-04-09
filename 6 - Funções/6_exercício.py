"""
Crie uma função que retorna se um número é maior
ou menor que 10;
O número deve ser passado como parâmetro;    
"""

a = 10
b = 9
c = 16

def maior_que_dez(nun):
    resultado = ""

    if nun > 10:
        resultado = "Maior que 10"
    elif nun < 10:
        resultado = "Menor que 10"
    else:
        resultado = "Igual a 10"

    return resultado

resultado_um = maior_que_dez(a)
print (resultado_um)

resultado_dois = maior_que_dez(b)
print (resultado_dois)

resultado_tres = maior_que_dez(c)
print(resultado_tres)


