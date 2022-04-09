"""
Crie um loop que detecta se um número é primo ou não
Número primo só é divido por 1 e ele mesmo;
"""

numero = int(input("Digite um número: "))

divisoes = 0

contador = numero

while contador > 0:

  if numero % contador == 0:
    divisoes = divisoes + 1

  contador = contador - 1 

if divisoes == 2:
  print("O número %d é primo!" % numero)
else:
  print("O número %d NÃO é primo" % numero)

"""
Lógica do código

Os números Primos são os números inteiros positivos 
divisíveis por um e por eles mesmos e maior ou igual a dois.

O número inserido pelo input sempre vai diminuindo por -1 
e em cada looop se o resto da divisao do número inserido pelo
input for zero, a variável divisão é somada + 1, nesse caso
identifica se o número é primo se o numero da variavel divisao
for igual a 2 se caso for menor ou maior não é primo.

"""
