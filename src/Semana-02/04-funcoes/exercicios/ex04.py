""" Exercício 04 """

def somar_args(*args):
    return sum(args)

resultado = somar_args(2, 4, 6.5, 1)
print(f"A soma dos números é: {resultado}")
