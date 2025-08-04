""" Exercício 03 """

identificador = input("Digite o identificador do funcionário: ")

if len(identificador) == 7:
    prefixo = identificador[:2]
    numero = identificador[2:6]
    sufixo = identificador[6]

    if prefixo == "BR" and sufixo == "X" and numero.isdigit():
        numero_int = int(numero)
        if 1 <= numero_int <= 9999:
            print("Identificador VÁLIDO")
        else:
            print("Identificador INVÁLIDO: número fora da faixa permitida.")
    else:
        print("Identificador INVÁLIDO: formato incorreto.")
else:
    print("Identificador INVÁLIDO: deve conter exatamente 7 caracteres.")
