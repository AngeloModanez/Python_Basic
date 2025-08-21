import math

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
soma = num1 + num2
sub = num1 + num2
div = num1 / num2
mul = num1 * num2

resto = num1 % num2
print(num1 // num2)
num1 += 1
print(f"Somando mais um ao primeiro valor: {num1}")

print("O resto final é:", soma)
print("A soma final é:", soma)
print(f"A subtração final é: {sub}")
print("A divisão final é: %d" % div)
print("A multiplicação final é: {}".format(mul))

# Exponenciação
expo = num1**num2

# Radiação
rad = math.sqrt(num1)

# Valor de pi
print(math.pi)

n = 0

print(math.cos(n))
print(math.sin(n))
