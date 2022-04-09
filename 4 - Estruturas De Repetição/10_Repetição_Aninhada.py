#Repetições Aninhadas
"""
Podemos inserir um loop dentro do outro;
A ordem de execução é de fora para dentro;
O loop interno será executado toda iteração do 
loop externo;
Temos que ter cuidado com os iteradores, precisamos 
de um para cada loop;
"""

i = 0

while i <= 10:
    print("i = %d" %i) 
    i = i + 1

    x = 0

    while x <= 5:
        print("x = %d" %x) 
        x = x + 1 
