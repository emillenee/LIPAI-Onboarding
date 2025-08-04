""" Exercício 01 """

# Solicite ao usuário 3 notas e apresente o resultado da média aritmética das notas

# Definir a quantidade de notas
QUANTIDADE = 3
notas = []

i = QUANTIDADE
indice = 1
while i>0 :
    nota = float(input(f'Digite a nota {indice}: '))
    notas.append(nota)
    i = i-1

total = 0.0
for nota in notas:
    total += nota

print(f'A média aritmética das notas é: {total / len(notas)}')
