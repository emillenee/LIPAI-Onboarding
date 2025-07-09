""" Aula 07 - Entrada e Saída de Dados """

# Saída padrão - sys stdout
print('hello world', 'Oscar', 1, True, sep=';', end='\n')

arquivo = open('nomes.txt', 'w', encoding='utf-8')
print('maria@email.com',
      'joao@email.com', 
      'pedro@email.com', 
      file=arquivo,
      sep=';'
    )

# Entrada - input
# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# print(type(nome), type(idade))

# if idade >= 18:
#     print(f'{nome}, você é maior de idade!')
# else:
#     print(f'{nome}, você é menor de idade.')

# File

# necessário criar um arquivo .txt com valores na pasta raiz
notas_arquivo = open('notas.txt', 'r', encoding='utf-8')
conteudo = notas_arquivo.read()
notas = conteudo.split(sep=';')
print(notas, type(notas))

# cálculo média 1
media = (float(notas[0]) + float(notas[1]) + float(notas[2])) / len(notas)
print(media)

# cálculo média 2
total = 0.0
for nota in notas:
    total = total + float(nota)
media2 = total / len(notas)
print(media2)

# map para converter todas as notas em float
notas = [float(nota) for nota in notas]
print(notas, type(notas))
