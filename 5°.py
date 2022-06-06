def soma_digitos(x):
    if int(x) < 10:
        return int(x)
    else:
        return soma_digitos(int(x) % 10) + soma_digitos(int(x) / 10)
 
numero = int(input("Digite um número: "))
while numero < 0:
    numero = int(input("Digite um número positivo: "))

resultado = soma_digitos(str(numero))    
print(f"A soma dos dígitos desse número é : {resultado}")
