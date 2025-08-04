""" Exercício 04 """

identificador = input("Digite o identificador do funcionário: ").strip()
erros = []


if len(identificador) != 7:
    erros.append("O identificador deve conter exatamente 7 caracteres.")
else:
    prefixo = identificador[:2]
    numero = identificador[2:6]
    sufixo = identificador[6]

    if prefixo != "BR":
        erros.append("O identificador não inicia com a sequência ‘BR’.")

    if not numero.isdigit():
        erros.append("A parte numérica do identificador deve conter apenas dígitos.")
    else:
        numero_int = int(numero)
        if not (1 <= numero_int <= 9999):
            erros.append("O identificador não apresenta número inteiro entre 0001 e 9999.")

    if sufixo != "X":
        erros.append("O identificador não finaliza com o caractere ‘X’.")

if not erros:
    print("Identificador VÁLIDO.")
else:
    print("Identificador INVÁLIDO. Erros encontrados:")
    for erro in erros:
        print(f"- {erro}")
        