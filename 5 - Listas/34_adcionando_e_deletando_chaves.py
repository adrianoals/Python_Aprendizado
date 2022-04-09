#Adicionando e deletando chaves
"""
Para adicionar um dicionário podemos simplesmente criar 
a nova chave a atribuir um valor;
Para deletar um item vamos utilizar a instrução del;

Veja:

del dicionario ["chave"]

"""

dic = {}

print (dic)

dic ["nome"] = "Mateus"

print (dic)

print(dic["nome"])

dic ["sobrenome"] = "Batisti"

print (dic)

del dic["nome"]

print (dic)



