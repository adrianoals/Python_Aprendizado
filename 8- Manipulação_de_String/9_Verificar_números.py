#Verificar se string é número
"""
Podemos verificar se uma string é composta por números com o 
método ' isdigit ';
Desta forma se a string conter apenas números teremos a resposta
True;
Caso haja outro caractere que não seja número recebemos False;
"""

numero = "123445"
print(numero.isdigit())

#O isdigit não identifica float apenas inteiros

frase = "asd"
print(frase.isdigit())

num2 = "134.67"
print(num2.replace(".","").isdigit())



