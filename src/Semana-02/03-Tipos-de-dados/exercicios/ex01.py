""" Exercício 01 """

numeros = []

for i in range(3):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

menor = min(numeros)
maior = max(numeros)

print(f"Menor número: {menor}")
print(f"Maior número: {maior}")