""" Aula 05 - Tipos de dados """

# Númericos
# int, float
idade = 20
peso = 60.5

print(idade, type(idade))
print(peso, type(peso))

# string
nome = 'Oscar'
sobrenome = 'Silva'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

produto = 'Cola-Cola'

print(f'O cliente {nome} {sobrenome} comprou o produto {produto}')

print(nome[0], nome[-1])

print(nome.lower())
print(nome.upper())

# boolean
ligado = True
print(ligado, type(ligado))

resultado = 10 < 3
print(resultado, type(resultado))

# Lista
# permite elementos duplicados
frutas = ['morango', 'manga', 'romã']
print(frutas)
print(frutas[0])
print(frutas[1])
print(frutas[2])
# print(frutas[3]) # Index Error

frutas[0] = 'morango silvestre'
frutas.append('melancia')
print(frutas)
print(len(frutas))

for fruta in frutas:
    print(fruta.upper())

# Tupla (Imutável)
codigos = ('SP01', 'SP02', 'SP03')
print(codigos[0])
# codigos[0] = 'SP05' # Type Error
print(len(codigos))

# Conjunto (set)
resultado_sorteio = {10, 4, 3, 55, 9}
print(resultado_sorteio)

resultado_sorteio.add(23)
print(resultado_sorteio)

# Dicionário
funcionario = {
    'codigo' : 123,
    'nome' : 'Oscar Silva',
    'salario' : 7000.00,
}
print(funcionario)
print(funcionario['codigo'])
print(funcionario['nome'])
print(funcionario['salario'])

print(funcionario.keys())
print(funcionario.values())

funcionario['salario'] = 9000.00
print(funcionario)
