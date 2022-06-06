def contadorLetras(frase:str):
    frase = frase.strip()
    if len(frase) == 0:
        return 0
    return 1 + contadorLetras(frase[1:])

p = str(input("Digite uma palavra: "))
print(f"Esse é a quantidade de letras que a palavra tem: {contadorLetras(p)}") 