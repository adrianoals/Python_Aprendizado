#Estrutura IF
"""
O " if " vai receber uma condição, que se for avaliada 
como verdadeira o software entra em um bloco de código
diferente;
Caso a condição não seja verdadeira, o bloco é ignorado;
A estrutura e a sintaxe é a seguinte:

Ex:
If condição:
    bloco a ser executado
"""

if 10>5:    
    verdura = "Cenoura"
    print("Entrou no If")
    print(verdura)

print("Antes do If")

if 10<5:    
    print("If Falso")

print("Depois do If")

nome = "Adriano"
idade = 33

if nome == "Adriano" and idade == 33:   
    print("Olá %s" % nome)

    
