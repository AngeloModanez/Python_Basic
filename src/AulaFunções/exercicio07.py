def somaImposto(taxa):
    global custo
    custo = custo + (custo * (taxa / 100))


custo = float(input("Digite o valor do custo: "))
taxaImposto = float(input("Digite o valor da taxa em porcentagem: "))
somaImposto(taxaImposto)
print(f"O valor do custo com o imposto é: {custo:.2f}")
