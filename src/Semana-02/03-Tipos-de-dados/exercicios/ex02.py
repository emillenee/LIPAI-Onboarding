""" Exercício 02 """

meses = (
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
)

numero = int(input("Digite o número do mês (1 a 12): "))

if 1 <= numero <= 12:
    print(f"Nome do mês: {meses[numero - 1]}")
else:
    print("Número inválido! Digite um valor entre 1 e 12.")