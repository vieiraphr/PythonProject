tentativas = 0

while tentativas < 3:
    senha = input("Crie sua melhor senha: ")

    numeros = sum(c.isdigit() for c in senha)
    tem_simbolo = any(c in "@#$%&!" for c in senha)
    tem_maiuscula = any(c.isupper() for c in senha)


    if len(senha) <8:
        print("Sua senha está muito curta, tente novamente.")
    elif len(senha) >16:
        print("Sua senha está longa, tente novamente.")
    elif numeros  <4:
        print("Sua senha precisa conter pelo menos 4 números.")
    elif not tem_simbolo:
        print("Sua senha precisa conter pelo menos 1 simbolo.")
    elif not tem_maiuscula:
        print("Sua senha precisa conter pelo mennos 1 letra maiúscula")
    else:
        print("SENHA CADASTRADA!")
        break  # sai do loop quando estiver válido

    tentativas += 1

if tentativas == 3:
    print("Número máximo de tentativas atingida.")

    #Projeto básico para aprimoramento de conhecimentos em Pytho