#Conversor de dados
"""
Os dados que vem da função input são do tipo string;
Ou seja, se quisermos utilizar um número para fazer 
uma soma vamos orecisar converter o tipo;
A função " int " vai converter para inteiro;
E a função " float " para ponto flutuante;
"""

numero_texto = input ("Digite um número ")

print (numero_texto)

novo_numero = 5 + int(numero_texto) 

print (novo_numero) 

