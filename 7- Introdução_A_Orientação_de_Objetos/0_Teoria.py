# O que é Orientação a Objetos?
"""
É um paradigma de programação, ou seja, uma forma diferente 
de programar;
Onde objetos interajam entre si;
Cada objeto tem características conhecidas como propriedades e
ações conhecidas como métodos;
Grandes frameworks do mercado são contruídos com Object-oriented programming
OOP, cono o Django;
"""
# O que é uma classe?
"""
As classes são moldes de objetos;
Então vamos criar uma classe que pode originar diversos objetos;
A classe originada pela palavra class;
Podemos adicionar propriedades e métodos a uma class, que serão utilizadas
por seus objetos;
A primeira letra da classe é sempre maiúscula;
"""
# O que são objetos?
"""
Um objeto é um filho de uma classe;
Ele poderá utilizar as propriedades e métodos que foram definidas 
na classe pai;
Após sua criação o objeto é independente da classe, podendo
alterar as propriedades isoladamente;
"""
#Adicionando Métodos
"""
Métodos são funções criadas para objetos;
Que podem interagir com o próprio objeto ou outros;
A palavra reservada self se trata sempre do objeto em si;
Iniciamos os métodos com def, como funções;
"""
#Herança
"""
Herança é um conceito de orientação de objetos;
Onde uma classe herda as propriedades e métodos de outra;
Assim seus objetos herdarão também estas características;
A classe que vai herdar deve receber como parâmetro esse pai;
"""
#Substituição de Métodos
"""
Em Python é possível substituir facilmente um método herdado;
Apenas precisamos declarar ele novamente na classe filha;
E então o método da classe filha que vale para seus objetos;
"""
#Métodos Mágicos
"""
Python tem mujitos métodos mágicos, um deles é o __str__;
Que serve para imprimir uma representação em string do que 
desejamos;
Podemos inserir este método __str__ em uma de nossas classes;
"""
#Propriedade Constantes
"""
Podemos também definir propriedades que não variam de
objeto em classe:
Ou seja, eles iniciam com um valor fixo;
Basta declarar fora de __self__ com algum valor;
"""
#Encapsulamento
"""
Encapsulamento é outro recurso da POO;
A ídeia é criar atributos privados que não podem ser alterados;
Fazemos isto em Python com _ou__ na frente dos métodos e variáveis;
Os atributos privados só são acessíveis por métodos do objeto;
"""
#Deletando Objetos
"""
Mais uma vez a instrução del é útil em Python;
Podemos deletar objetos por meio de del obj;
Após interpretada a linha de código, não podemos mais
acessar nem propriedades e nem métodos do objeto
removido;
"""