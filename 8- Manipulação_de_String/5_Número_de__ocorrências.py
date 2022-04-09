# Número de ocorrências
"""
Podemos contar o número de ocorrências de uma determinada
string em outra;
Para este fim utilizamos a função count;
Ela nos retorna o número da palavras encontradas;
"""
texto = "Está é a frase que vamos checar a ocorrência da palavra frase"

print(texto.count("frase"))

if texto.count("frase") == 2:
    print("A contagem está correta!")

print(texto.count("Olá"))

contador = texto.count("frase")
print(contador)
