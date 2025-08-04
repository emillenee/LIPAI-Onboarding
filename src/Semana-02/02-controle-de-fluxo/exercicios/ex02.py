""" Exercício 02 """

entrada = input("Digite suas notas separadas por vírgula (ex: 7.5, 8.0, 6.3): ")

notas = [float(n.strip()) for n in entrada.split(",")]

media = sum(notas) / len(notas)

if media > 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
