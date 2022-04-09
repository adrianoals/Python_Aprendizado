"""
Escreva uma função que recebe um dado de texto;
Se esse dado tem mais de 20 caracteres, retorne que é um texto longo;
Se tem menos, retorne que é um texto curto;

"""

texto_um = "Precisa controlar a ansiedade"
texto_dois = "Paciencia"

def func(texto):
    frase = ""
    if len(texto) > 20:
        frase = "Esse texto é longo"
    else:
        frase = "Esse texto é curto"
  
    return frase 

frase_1 = func(texto_um)
print (frase_1)

frase_2 = func(texto_dois)
print (frase_2)

print(func("E ae José"))


