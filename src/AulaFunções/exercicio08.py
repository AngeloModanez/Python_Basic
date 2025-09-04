def classeEleitoral(i):
    if i < 16:
        return "Não é eleitor"
    elif i < 18 or i > 65:
        return "Eleitor facultativo"
    else:
        return "Eleitor obrigatório"


idade = int(input("Digite sua idade: "))
print(classeEleitoral(idade))
