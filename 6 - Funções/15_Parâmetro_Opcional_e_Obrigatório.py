#Parâmetro Opcional e Obrigatório
"""
Podemos ter funções com parâmetros opcionais e obrigatórios;

Ou seja, cada parâmetro é independente um do outro;

Obs: Os parâmetros opcionais devem sempre estar depois dos
obrigatórios;

Veja um exemplo:

def teste(x, y = 10):
    print (x + y)

"""
def soma_numeros(a, b, c = 10):
    print (a + b + c)

soma_numeros(1, 2, 3)

soma_numeros(10, 20)

#Dar erro pois b é obrigatório
"""
def soma_numeros_2(a, b, c = 10):
    print (a + b + c)
soma_numeros_2(10)
"""
#Dar erro pois o parâmetro opcional tem que vir depois do obrigatório
"""
def soma_numeros_2(a=10, b, c = 10):
    print (a + b + c)
soma_numeros_2(10)
"""