def triangulo(b, a):
    return (b * a) / 2


base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
area = triangulo(base, altura)
print(f"A área do triangulo é: {area}")
