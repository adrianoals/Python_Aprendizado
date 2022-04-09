#Verificando chaves
"""
Podemos checar se uma chave existe em um dicionário
utilizando o operador in;
recebemos um boolean desta operação;
É possível utilizar esta sentença em um if, por exemplo;

Veja a sintaxe:

    print("item_1" im itens)

"""

dicionário = {
    "testando": 2,
    "Nome": "Matheus",
    "Idade": "29"
}

print(dicionário)

print("Nome" in dicionário)
print("Sobrenome" in dicionário)

if "Nome" in dicionário:
    print("O seu nome é %s" % dicionário["Nome"])

if "Sobrenome" in dicionário:
    print ("O seu sobrenome é %s" % dicionário["Sobrenome"])

else:
    print ("Não tem sobrenome.")