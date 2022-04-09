#Operador And
"""
O operador "and" vai comparar um booleano com outro;
Podemos utilizar com duas comparações;
O resultado do operador and será um boolean;
O and só retorna True e se ambos os valores forem True

 A     B     A and B  
 0     0        0
 0     1        0
 1     0        0
 1     1        0
"""

a = 5
b = 10
c = 2
d = 8

print (a > b and c > d)
print (a > b and c < d)
print (c < d and b < c)
print (a < b and b > c)