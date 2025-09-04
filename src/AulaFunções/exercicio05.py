def circle(r):
    pi = 3.14159
    a = pi * r**2
    return a


raio = float(input("Digite o valor do raio: "))
area = circle(raio)

print(f"o Valor da área: {area}")
