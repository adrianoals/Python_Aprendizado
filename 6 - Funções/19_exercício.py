"""
Crie uma função que recebe uma sequência de 
parâmetros númericos
Multiplique todos eles e exiba o valor no terminal;
"""
def mult_todos(*numeros):
    mult = 1
    for nun in numeros:
        mult *= nun 
    return mult 

s = mult_todos(1, 2, 3)

print(s)
