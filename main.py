tentativas = 0

while tentativas < 3:
    nome = input("Digite seu username: ")

    if len(nome) <8:
        print("Curto demais, tente novamente.")
    elif len(nome) < 10:
        print("Ok")
        break  # sai do loop quando estiver válido
    else:
        print("Muito longo, tente novamente!")

    tentativas += 1

if tentativas == 3:
    print("Número máximo de tentativas atingida.")