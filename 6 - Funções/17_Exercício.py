"""
Crie uma função que receba outra como parâmetro;
A que vai receber parâmetros deve receber um nome, uma 
idade e uma profissão;
A função argumento deve apresentar estes dados em uma
string dinâmica.
"""

def reune_dados(nome, idade, profissao, fnct):
    apresentacao = fnct (nome, idade, profissao)
    return apresentacao

def apresenta_dados(nome, idade, profissao):
    frase = "O nome do usuário é %s e sua idade é %d anos e ele é um %s" %(nome, idade, profissao)
    return frase

print (reune_dados("Adriano", 33, "Programador", apresenta_dados))

apresentacao = reune_dados("Pedro", 40, "Engenheiro", apresenta_dados)
print(apresentacao)


