""" Aula 06 - Conversão de Tipos """

# Implícita e Explícita

leitura = 5.53
peso = 3
total = leitura * peso
print(total, type(total))

# type casting
soma = 13.4 + float('3.5')
print(soma, type(soma))

idade = '32'
print(idade, type(idade))
idade = int('32')
print(idade, type(idade))

nome = 'Raquel'
altura = 1.72

# mensagem = nome + ' tem a altura de ' + str(altura)
mensagem = f' {nome} tem a altura de {altura}'
print(mensagem)
