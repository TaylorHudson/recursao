def quadrados(n):
    if n == 0:
        return ""
    if n >= 1:
        lista.append(n*n)
        quadrados(n-1)

    return lista
    
lista = []
print(quadrados(10))

