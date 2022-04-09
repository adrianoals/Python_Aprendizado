#Erros de conversão de dados
"""
Caso o usuário insira um tipo de dado não 
esperado pelo input o Python vai nos retornar
um erro;
Por exemplo:
Esperamos um número e é inserida uma string;
Outro erro comum é vírgula nos pontos flutuantes,
onde o Python espera um ponto;
"""

numero = int(input("Digite um número "))
# E o usuário digita uma string.

salario = float(input("Digite o seu salário "))
# E o usuário digita com virgula separando as casas decimais.