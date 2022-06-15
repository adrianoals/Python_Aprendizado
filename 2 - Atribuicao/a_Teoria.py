# O que são variaveis
"""
Uma forma de armazenar valores na memória;
Podemos utiliza-lás posteriormente em nossos programas

Cada variável terá um tipo de dado;
Por exemplo: "teste" => texto e 14 => número

Os tipos de dados são muito importantes na programação;

As vezes precisamos garantir que por meio de testes que uma variável
tem determinado tipo  
"""

#Atribuindo valores
"""
Colocar um valor em uma variável é chamado de atribuição em programação
Podemos exibir um valor de uma variável com a função "print"
Ex: 
nome = "Matheus"
print (nome)

E com a função "type" podemos descobrir o tipo da variável
"""

#Nomes Válidos
"""
Nem todos caracteres são aceitos para criar nomes de variáveis;
Utilize esses mesmos critérios para nomear arquivos Python;

Veja os nomes válidos; 
Ex: teste1, nome, ano2020, nome_completo, _idade

Veja agora os inválidos
Ex: palavra separada, 5nome, @nome

Diretrizes válidas: Começar com string ou _ e seperar com _
"""

#Valores númericos
"""
É possível inserir números em variáveis também;
Temos os inteiros ex: 1, 950, 99999

E temos os de pontos flutuantes ex: 1.50, 250.90, 0.99999009

Obs: Na maioria das linguagens utiliza o "ponto" para separar as casas decimais 
"""

#Valores Booleanos
"""
O tipo de dado Boolean se resume a "True" e "False", ou seja verdadeiro e falso;
Podemos criar variáveis com esses valores;
E eles serãom úteis mais para frente, quando criarmos programas 
que tem condições de de comparação;
"""

#Operadores Relacionais
"""
Também conhecidos como operadores de comparação, vão auxiliar 
os testes que fazemospor meio de comparação de dois valores;

Temos os seguintes operadores: == , != , > , < , >= , <=
E utilizamos da seguinte maneira:
Ex: 5 > 3
O resultados das comparações é sempre booleano
"""
#Operadores Lógicos
"""
Temos três operadores lógicos: not, and e or;
Que são representados por estas palavras, ou seja, não há símbolos;
Em outra linguagens é comum ter símbolos para esses operadores
Eles podem unir duas comparações de operadores lógicos ou inverter po valor de alguma;

Obs: em outras linguagens o not é ! , o and é & , e o or é ||

"""
#Operador Not
"""
O operador "not" vai inverter o valor de uum booleano;
Ou seja, quando criarmos um comparação que resulta em
booleano, podemos inverter com not;
"True" se torna "False" e "False" se torna "True"
 A  Not A
 1    0
 0    1
"""

#Operador And
"""
O operador "and" vai comparar um booleano com outro;
Podemos utilizar com duas comparações;
O resultado do operador and será um boolean;
O and só retorna True e se ambos os valores forem True

 A     B     A and B  
 0     0        0
 0     1        0
 1     0        0
 1     1        0
"""

#Operador Or
"""
O operador "or" vai comparar um booleano com outro;
Podemos utilizar com duas comparações;
O resultado do operador and será um boolean;
O or só retorna False e se ambos os valores forem False

 A     B     A and B  
 0     0        0
 0     1        1
 1     0        1
 1     1        1
"""
#Expressões Lógicas
"""
Os operadores lógicos podem ser combinados em expressões lógicas;
As expressões lógicas consistem em duas comparações com um operador 
lógico entre estas;
Desta maneira resumimos o código e também  podemos criar
mais variedades de comparação:
Ex:
idade > 18 and passaporte == True
"""
#Variáveis com Texto
"""
Os textos geralmente na programação são chamados de string;
Uma string é caracterizado por textos entre aspas;
As string servem tanto para textos menores como também
para textos maiores:
Ex:
profissao = "programador"
Podemos identificar o tamanho de uma string
com a função " len() "
"""
#Acessando Caracteres de uma string
"""
Podemos acessar o caractere de uma string;
Para isso precisamos saber o índice do caractere;
O índice é a posição de uma letra, e sempre começa por 0;
Então a primeira letra têm o índice 0;
Cso índice não exista em uma string, recebemos um erro 
mo Python;
Ex:
print(palavra[3])
"""
#Comtatenação
"""
A a ação de juntar uma sgring é chamada de concatenação;
É um recurso muito utilizado, ainda mais em conjunto de 
variáveis;
Podemos formar frases unir duas variáveis, por exemplo;
O simbolo de concatenação no Python é o +
"""
#Strings dinâmicas
"""
Podemos inserir variáveis em string de outra maneira;
E assim deixa-lás dinâmicas, compondo elas com valores
diferentes;
O símbolo de composição é o %
Porém cada tipo de dado tem um caractere diferente em 
seguida do % => " d " para inteiros, " s " para string e " f " para floats
"""
#Strings dinâmicas com float
"""
Para inserir os decimais temos uma sintaxe um pouco 
diferente dos demais tipos de dados;
Por causa do número de casas decimais que vamos 
exibir;
Exemplo:
print("Você deve R$%.2f ao banco." %valor)
""" 
#Manipulação de uma string / decomposição
"""
Podemos resgatar uma parte da string atravéz 
dos índices dos caracteres;
Está pratica é bem útil conhecida também como 
manipulação de string;
Exemplo:
print(frase[0:5]) => Resgatando do primeiro ao quinto índice;
"""
#Decomposição de string 
"""
Se omitirmos o valor da esquerda ou da direita
o python vai entender que queremos resgatar algo 
desde do ínicio ou até o fim;
Ex: 
print (frase[:5])

Podemos incluir funções negativas, que o 
Python vai cortar pela direita:
print(frase[-2:0])
"""
#Input de dados
"""
Podemos inserrir dados nos programas que criamos;
Esta ação é feita por meio da função " input "
Este dado pode ser armazenado em um variável;
E podemos exibi-lo com " print ", da mesma forma 
como estamos fazendo até o momento
Exemplo:
numero = input("Digite um número: ")
"""
#Conversor de dados
"""
Os dados que vem da função input são do tipo string;
Ou seja, se quisermos utilizar um número para fazer 
uma soma vamos orecisar converter o tipo;
A função " int " vai converter para inteiro;
E a função " float " para ponto flutuante;
"""
