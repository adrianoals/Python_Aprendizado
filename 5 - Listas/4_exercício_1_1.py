#Exercício: 
"""
Crie uma lista com 5 notas de uma prova de um aluno;
Faça um loop que calcula a média das notas;
Imprima o resultado final;
"""
notas = [6.5, 7, 8, 9, 6]

x = 0
soma_notas = 0
prova = 1

while x < 5:
    print ("A nota da prova %d é %.1f" %(prova, notas[x]))#Apenas p/ vizualização
    soma_notas = soma_notas + notas[x]
    prova = prova + 1
    print ("A soma das notas é %.1f" %soma_notas) #Apenas p/ vizualização
    x = x + 1

media = soma_notas / 5
print ("A média final do aluno é %.1f" % media) 

   