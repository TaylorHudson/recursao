def concatenandoRec(letras:list):
    if len(letras) == 1:
        return letras[0]
    else:
        primeira = letras.pop(0)
        return primeira + concatenandoRec(letras) 

lista = list(str(input("Digite letras: ")))
print(concatenandoRec(lista))
