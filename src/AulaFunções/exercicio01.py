def bunda(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None


n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

maior = bunda(n1, n2)

if maior:
    print(f"O maior valor é: {maior}")
else:
    print("Os dois valores são iguais")
