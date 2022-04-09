#O que são funções
"""
Já utilizamos diversas fuções no Python: print, len, float, input;
A ídeia principal é criar um bloco de código reutilizável
Assim podemos chamar a função em qualquer lugar e reutilizar 
sua lógica;
O ínicio da função é feito por def, veja sua sintaxe:

def digaoi(nome):
    print("Oi %s" %nome)

"""
#Retornando valores
"""
As funções normalmente retornam valores, por meio da instrução
return;
O retorno pode ser inserido em uma variável e utilizado 
posteriormente no nosso software;
Sintaxe:

def função(x):
    return (x + 1)
"""
# Escopo 
"""
Quando estamos dentro do bloco de função temos um escopo local;
As variáveis dessa função não podem ser utilizdas em outra;
Quando estamos fora da função estamos no escopo global;
As variáveis do escopo global podem ser utilizadas em funções;
"""
#Função recursiva
"""
O recurso da função recursiva é quando uma função chama a si mesma;
Temos que ter cuidado pois pode ser criado um loop infinito aqui também;
A função recursiva tem algumas situações de uso, mas não é tão comum assim;
"""
#Parâmetro opcional
"""
As funções podem ser criadas com parâmetros opcionais, ou 
seja um valor pode já estar preenchido para um parâmetro;
Então podemos utilizar a função sem passar o valor do 
parâmetro;
O que pode ser útil em alguns casos, quando já temos valores 
padronizados;

Veja a sintaxe:

def teste(x=10):
    print(x)
     
"""
#Parâmetro Opcional e Obrigatório
"""
Podemos ter funçãoes com parâmetros opcionais e obrigatórios;

Ou seja, cada parâmetro é independente um do outro;

Obs: Os parâmetros opcionais devem sempre estar depois dos
obrigatórios;

Veja um exemplo:

def teste(x, y = 10):
    print (x + y)

"""
#Parâmetro Opcional e Obrigatório
"""
Podemos ter funções com parâmetros opcionais e obrigatórios;

Ou seja, cada parâmetro é independente um do outro;

Obs: Os parâmetros opcionais devem sempre estar depois dos
obrigatórios;

Veja um exemplo:

def teste(x, y = 10):
    print (x + y)

"""
#Funções como Parâmetro
"""
Podemos inserir funções como parâmetros para outras funções;

Desta maneira podemos gerar mais reaproveitamento de código;

Proporcionando uma função utilizar várias outras apenas 
adicionando um argumento diferente na execução;
"""
#Sequência de Parâmetros
"""
Podemos inserir uma série de parâmetros ma hora de criar
uma função;

Se estes forem do mesmo tipo, podem ajudar a criar uma função
que pode processar diversos parâmetros, veja:

def funcao (argumentos)
for x in argumentos:
    print(x)
"""
# Função Lambda
"""
A função lambda vem da programação funional;
Podemos criar uma função que executa uma simples expressão;
E atribuir o valor obtido a uma variável, veja:

x = lambda a: a + 10

print(x(10))
"""
#Módulos
"""
Módulo é o recurso que temos para exportar o conteúdo de um
arquivo e importar outro;
Ou seja, podemos dividir nosso programa em vários arquivos
com funções diferentes;

Veja a sintaxe:
import arquivo

"""
#Função Randint
"""
Com randint podemos gerar números aletórios;
Isso pode ser útil em algumas situações, como sorteios por exemplo;
Esta função faz parte do módulo ramdom;

Veja um exemplo:

import ramdom 

print(ramdom.randit(1,10))
"""
