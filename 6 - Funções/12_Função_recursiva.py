#Função recursiva
"""
O recurso da função recursiva é quando uma função chama a si mesma;
Temos que ter cuidado pois pode ser criado um loop infinito aqui também;
A função recursiva tem algumas situações de uso, mas não é tão comum assim;
"""

def soma_ate_100(n):
    if n < 100:
        n += 1
        print(n)
        return soma_ate_100(n)
    else:
        return "Dome.."

numero = 94

nun_100 = soma_ate_100(numero)
print (nun_100)



