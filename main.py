import json
import hashlib
import os
import re

ARQUIVO = "usuarios.json"


# ================= ARQUIVO =================

def carregar_usuarios():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}


def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w") as f:
        json.dump(usuarios, f, indent=4)


usuarios = carregar_usuarios()


# ================= SEGURANÇA =================

def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


# ================= VALIDAÇÕES =================

def validar_email(email):
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(padrao, email) is not None


def validar_username(username):
    if len(username) < 5:
        print("Username muito curto")
        return False
    elif len(username) > 15:
        print("Username muito longo")
        return False
    elif not username.isalnum():
        print("Use apenas letras e números")
        return False
    elif username in usuarios:
        print("Username já existe!")
        return False
    return True


def validar_senha(senha):
    numeros = sum(c.isdigit() for c in senha)
    tem_simbolo = any(c in "@#$%&!" for c in senha)
    tem_maiuscula = any(c.isupper() for c in senha)

    if len(senha) < 8:
        print("Senha muito curta")
        return False
    elif len(senha) > 16:
        print("Senha muito longa")
        return False
    elif numeros < 4:
        print("Precisa de pelo menos 4 números")
        return False
    elif not tem_simbolo:
        print("Precisa de símbolo")
        return False
    elif not tem_maiuscula:
        print("Precisa de maiúscula")
        return False

    return True


# ================= CRIAÇÃO =================

def criar_username():
    while True:
        username = input("Digite um username: ")

        if username == "0":
            print("Voltando ao menu...")
            return None

        if validar_username(username):
            return username


def criar_email():
    while True:
        email = input("Digite um email: ")

        if email == "0":
            print("Voltando ao menu...")
            return None

        if not validar_email(email):
            print("Email inválido! Exemplo: nome@email.com")
        elif any(dados["email"] == email for dados in usuarios.values()):
            print("Email já cadastrado!")
        else:
            return email


def criar_senha():
    while True:
        senha = input("Crie sua senha: ")

        if senha == "0":
            print("Voltando ao menu...")
            return None

        if validar_senha(senha):
            confirmar = input("Confirme a senha: ")

            if senha == confirmar:
                return criptografar_senha(senha)
            else:
                print("Senhas não coincidem")


# ================= AÇÕES =================

def cadastrar():
    print("\n--- CADASTRO ---")
    print("Digite 0 a qualquer momento para voltar ao menu\n")

    username = criar_username()
    if not username:
        return

    email = criar_email()
    if not email:
        return

    senha = criar_senha()
    if not senha:
        return

    usuarios[username] = {
        "email": email,
        "senha": senha,
        "tentativas": 0
    }

    salvar_usuarios(usuarios)
    print("Cadastro realizado com sucesso!")


def buscar_usuario(login):
    for user, dados in usuarios.items():
        if user == login or dados["email"] == login:
            return user
    return None


def login():
    print("\n--- LOGIN ---")
    print("Digite 0 a qualquer momento para voltar ao menu\n")

    login_input = input("Digite seu username ou email: ")

    if login_input == "0":
        print("Voltando ao menu...")
        return

    usuario = buscar_usuario(login_input)

    if not usuario:
        print("Usuário não encontrado")
        return

    while usuarios[usuario]["tentativas"] < 5:
        senha = input("Digite sua senha: ")

        if senha == "0":
            print("Voltando ao menu...")
            return

        senha_criptografada = criptografar_senha(senha)

        if usuarios[usuario]["senha"] == senha_criptografada:
            print("Login realizado com sucesso!")
            usuarios[usuario]["tentativas"] = 0
            salvar_usuarios(usuarios)
            return
        else:
            usuarios[usuario]["tentativas"] += 1
            restantes = 5 - usuarios[usuario]["tentativas"]

            print("Senha incorreta")
            print(f"Tentativas restantes: {restantes}")

    print("Acesso bloqueado.")
    salvar_usuarios(usuarios)


# ================= MENU =================

def menu():
    print("\n1 - Cadastrar")
    print("2 - Login")
    print("3 - Sair")
    return input("Escolha: ")


# ================= PROGRAMA =================

while True:
    opcao = menu()

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        login()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida")