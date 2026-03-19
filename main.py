usuarios = {}

while True:
    print("\n1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")

    opcao = input("Escolha: ")

    # ================= CADASTRO =================
    if opcao == "1":
        username = input("Digite um username: ")
        email = input("Digite um email: ")

        if username in usuarios:
            print("Username já existe!")
            continue

        tentativas = 0

        while tentativas < 3:
            senha = input("Crie sua senha: ")

            numeros = sum(c.isdigit() for c in senha)
            tem_simbolo = any(c in "@#$%&!" for c in senha)
            tem_maiuscula = any(c.isupper() for c in senha)

            if len(senha) < 8:
                print("Senha muito curta")
            elif len(senha) > 16:
                print("Senha muito longa")
            elif numeros < 4:
                print("Precisa de pelo menos 4 números")
            elif not tem_simbolo:
                print("Precisa de símbolo")
            elif not tem_maiuscula:
                print("Precisa de maiúscula")
            else:
                confirmar = input("Confirme a senha: ")

                if senha == confirmar:
                    usuarios[username] = {
                        "email": email,
                        "senha": senha
                    }
                    print("Cadastro realizado com sucesso!")
                    break
                else:
                    print("Senhas não coincidem")

            tentativas += 1

        if tentativas == 3:
            print("Falha ao criar senha.")

    # ================= LOGIN =================
    elif opcao == "2":
        tentativas_login = 0

        while tentativas_login < 5:
            login = input("Digite seu username ou email: ")
            senha = input("Digite sua senha: ")

            usuario_encontrado = None

            # 🔍 procurar usuário
            for user, dados in usuarios.items():
                if user == login or dados["email"] == login:
                    usuario_encontrado = user
                    break

            if usuario_encontrado:
                if usuarios[usuario_encontrado]["senha"] == senha:
                    print("Login realizado com sucesso!")
                    break
                else:
                    print("Senha incorreta")
            else:
                print("Usuário não encontrado")

            tentativas_login += 1
            print(f"Tentativas restantes: {5 - tentativas_login}")

        if tentativas_login == 5:
            print("Acesso bloqueado.")

    # ================= SAIR =================
    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida")