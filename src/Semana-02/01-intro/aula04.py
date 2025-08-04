""" Aula 04 - Variáveis, constantes, literais """

# Variável
# inferência de tipo
numero = 10
print(numero, type(numero))

# multiplas atribuições - prática não recomendada
nome, idade, endereco = 'Raquel', 23, 'Saraiva'
print(nome, idade, endereco)

# atribuir mesmo valor para várias variáveis
nome1 = nome2 = nome3 = 'Emily'
print(nome1, nome2, nome3)

nome2 = 'Oscar'
print(nome1, nome2, nome3)

#snake_case
id_funcionario = 290
salario_atual = 5000.50
print(id_funcionario, salario_atual)

# Constantes
# Upper case e snake case

PI = 3.14
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 21
print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# Literais

idade = 27
print(idade)
print(27)

# númericos
print(10, type(10))
print(-10, type(-10))
print(10.5, type(10.5))

# string
print('Maria', type('Maria'))
print("Maria", type("Maria"))
print("John's house")
print('O filme estava "excelente"')

# booleano
print(True, type(True))
print(False, type(False))

# none
print(None, type(None))

# Coleções

# Lista (Mutável)
numeros = [1, 3, 5]
print(numeros, type(numeros))

# Tupla
emails = ('@gmail.com', '@outlook.com')
print(emails, type(emails))

# Conjunto (set)
nomes = {'maria', 'joao', 'pedro', 'maria'}
print(nomes, type(nomes))

# Dicionário
aluno = {
    'prontuario' : 123456,
    'nome' : "Raquel Emillene",
    'idade' : 23,
}
print(aluno, type(aluno))
