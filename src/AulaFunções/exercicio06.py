def isPositive(v):
    if v >= 0:
        return "P"
    else:
        return "N"


valor = int(input("Digite um valor negativo ou positivo: "))
resultado = isPositive(valor)

print(resultado)
