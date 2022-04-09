#Listas
"""
Lista é outro tipo de dado em Python
Em outras linguagens é comum ter o nome de Array;
Podemos entender uma lista como conjunto de elementos;
Que pode estar vazia ou não e também possui índice para 
cada um dos seus elementos;
"""
#Acessando e modificando listas
"""
Podemos acessar os elementos de uma lista pelos 
índices dos mesmos, começando do zero;

Exemplo:
print (lista[2])

A modificação de um elemento de uma lista é por meio da
identificação do índice do mesmo e atribuição de novo
valor;

Exemplo:
lista[2] = "novo valor"
"""
#Percorrendo lista com um loop
"""
Podemos percorrer uma lista com um loop;
E acessar cada índice por iteração na lista;
Desta forma podemos escrever programas baseados 
em uma lista de valores;
"""
#Cópia de lista
"""
#Tomar cuidado ao copiar uma lista
#Se atribuirmos um valor de uma a outra diretamente a segunda será uma referencia da primeira
#Replicando as alterações, ou seja, serão a mesma lista
"""
#Cópia Lista sem referência 
"""
#Para copiar uma lista sem referência, podemos utilizar
uma sintaxe especial;
Parecida com a quais utilizamos para resgatar caracteres
de uma string, com intervalos de índices;
Exemplo:

lista_dois = lista_um[:]
"""
#Fatiando Lista
"""
Semelhantes as strings, podemos resgatar só determinados 
elementos com decomposição por índice;

Precisamos passar o índice inicial e final para o Python,
e teremos uma nova lista com os elementos selecionados;

Exemplo:
lista_nova = lista[3:6]
"""
#Quantidade de Elementos
"""
Podemos identificar a quantidade de elementos de uma lista
com a função " len() ";
Desta forma podemos aplicar alguma lógica relacionada ao 
tamanho das listas;
Esta função também é aplicada em strings;
"""
#Loop com len
"""
Utilizando o comprimento da lista, podemos fazer um loop nela 
sem precisar contar os índices;

Isso torna nosso código dinâmico, que aceita qualquer tamanho de lista;

Exemplo: 
while a < len(lista):
"""
#Incrementando listas / Adicionando Elementos na lista
"""
Podemos incrementar listas utilizando a função append;
Um elemento será adicionado ao fim da lista;
Esta é uma das formas mais usadas para adicionar 
elementos a uma listas;

Exemplo:
lista.append(2)
"""
#Removendo elementos
"""
Podemos remover elementos com a instrução " del ";
Vamos precisar também do índice do elemento a ser removido;

Veja a sintaxe:

del lista[3]

"""
#Buscando elementos na lista
"""
Podemos criar um loop que busca um elemento em um array;
A ídeia é: percorrer todos os índices e verificar se o 
elemento é igual ao elemento do índice;

Veja:

while condição:
    if lista[i] == elemento 
    print ("Encontrado")
"""
# For com listas
"""
O for funciona muito bem com listas;
Não precisamos criar um contador, pois ele percorre todos
os elementos;

Veja a sintaxe:

for x lista:
    print(x)

"""
#Range
"""
Com range podemos criar loops semelhantes ao while;
Ou seja, não dependemos de uma lista;
Veja a sintaxe de range;

for x in range(5)
print(x)

"""
#Incremento do range
"""
Podemos adicionar um ínicio e fim para o range;
Como também podemos alyterar o incremento;

Veja a sintaxe de range com incremento:

for x in range(0, 20, 2):
    print(x)
"""
#Verificando maior valor
"""
Podemos verificar o maior valor de uma lista facilmente com for;
Faremos um loop em uma lista, e checamos se o valor atual é 
maior que o maior valor;
Este maior valor deve ser inicializado com um valor de 0;

Veja:

maior_valor = 0 
for x in lista:
    if x> maior_valor
    maior_valor = x
"""
#Listas com listas
"""
É possível inserir uma lista dentro de outra lista em Python;
Primeiramente criamos as listas internas e depois podemos 
constituir uma nova lista com estes itens;

Veja:

lista_pai =[lista_a, lista_b]

"""
#Dicionários
"""
O dicionário é semelhante a lista, porém o item possui 
uma chave e um valor;
Essa estrutura é semelhante ao array associativo de 
outras linguagens;

Veja a sintaxe:

notas{
    "prova_1":10,
    "prova_2":8,
    "prova_3":9
}

"""
#Verificando chaves
"""
Podemos checar se uma chave existe em um dicionário
utilizando o operador in;
recebemos um boolean desta operação;
É possível utilizar esta sentença em um if, por exemplo;

Veja a sintaxe:

    print("item_1" im itens)

"""
#Adicionando e deletando chaves
"""
Para adicionar um dicionário podemos simplesmente criar 
a nova chave a atribuir um valor;
Para deletar um item vamos utilizar a instrução del;

Veja:

del dicionario ["chave"]

"""
#Tuplas
"""
As tuplas são consideradas listas em Python;
A sua grande difereça é que seus dados são imutáveis;
Podemos acessar os elementos pelos índices como o array

Veja a sintaxe:

tupla = (1, 2, 3)
""" 
#Iterando Tuplas
"""
Podemos iterar nas tuplas como nas listas com for;
Utilizamos a mesma sintaxe, o Python não faz distinção dos dois
tipos de dados;

Exemplo:

for x tupla:
    print(tupla[x])

"""