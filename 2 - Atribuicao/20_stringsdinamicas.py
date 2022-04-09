#Strings dinâmicas
"""
Podemos inserir variáveis em string de outra maneira;
E assim deixa-lás dinâmicas, compondo elas com valores
diferentes;
O símbolo de composição é o %
Porém cada tipo de dado tem um caractere diferente em 
seguida do % => " d " para inteiros, " s " para string e " f " para floats
"""

nome = "Adriano"

print ("Olá, meu nome é %s" %  nome)

idade = 29

print ("Eu tenho %d anos." % idade)

carro = "Ferrari"
ano = 2000

print ("O meu carro é uma %s e foi fabricado no ano %d" % (carro, ano))