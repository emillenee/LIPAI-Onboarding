""" Exercício 03 """

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

numero = int(input("Digite o número do mês (1 a 12): "))

if numero in meses:
    print(f"Nome do mês: {meses[numero]}")
else:
    print("Número inválido! Digite um valor entre 1 e 12.")