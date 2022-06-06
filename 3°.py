def contadorA(frase:str):
    frase = frase.upper()
    if frase == "":
        return 0
    elif frase[0] == "A":
        return 1 + contadorA(frase[1:])
    return contadorA(frase[1:])

palavra = str(input("Digite uma frase: "))
print(contadorA(palavra))
         