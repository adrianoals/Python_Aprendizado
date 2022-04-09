#Exercício: 
"""
# Crie uma lista com 5 notas de uma prova de um aluno;
#Faça um loop que calcula a média das notas;
#Imprima o resultado final;
"""
notas = [6.5, 7, 8, 9, 10]

x = 0
soma_notas = 0
print (notas) #Apenas p/ vizualização
    
while x < 5:
    soma_notas = soma_notas + notas[x]
    print (soma_notas) #Apenas p/ vizualização
    x = x + 1

media = soma_notas / 5
print ("A média do aluno foi de %.2f" % media) 
