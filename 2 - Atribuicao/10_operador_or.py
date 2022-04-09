#Operador Or
"""
O operador "or" vai comparar um booleano com outro;
Podemos utilizar com duas comparações;
O resultado do operador and será um boolean;
O or só retorna False e se ambos os valores forem False

 A     B     A and B  
 0     0        0
 0     1        1
 1     0        1
 1     1        1
"""
a = 5
b = 20

print (a > b or b == 11)
print (b > a or b == 10)
print (b > a or b == 20)
print (b > a or b == 10)

