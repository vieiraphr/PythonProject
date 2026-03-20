🔐 Sistema de Cadastro e Login em Python

Este é um sistema simples de autenticação desenvolvido em Python, que permite o cadastro e login de usuários com validações e armazenamento em arquivo JSON.

📌 Funcionalidades

✅ Cadastro de usuários

✅ Login com username ou email

✅ Criptografia de senha com SHA-256

✅ Validação de:

Username

Email

Senha forte

✅ Controle de tentativas de login (bloqueio após 5 erros)

✅ Persistência de dados em arquivo (usuarios.json)

🛠️ Tecnologias utilizadas

Python 3

Bibliotecas padrão:

json

hashlib

os

re

📂 Estrutura do Projeto
📁 projeto
│-- usuarios.json   # Base de dados dos usuários
│-- main.py         # Código principal do sistema
🔒 Regras de Validação
Username

Deve ter entre 5 e 15 caracteres

Apenas letras e números

Não pode existir previamente

Email

Deve seguir o padrão: nome@email.com

Não pode ser duplicado

Senha

Entre 8 e 16 caracteres

Pelo menos 4 números

Pelo menos 1 letra maiúscula

Pelo menos 1 símbolo: @#$%&!

🔐 Segurança

As senhas são armazenadas com criptografia usando SHA-256

O sistema limita tentativas de login:

Máximo de 5 tentativas

Após isso, o acesso é bloqueado

▶️ Como executar

Certifique-se de ter o Python instalado

Execute o arquivo principal:

python main.py
💡 Como usar
Menu principal:
1 - Cadastrar
2 - Login
3 - Sair
Cadastro

Crie um username, email e senha seguindo as regras

Login

Pode usar:

Username ou

Email

📌 Melhorias futuras (EM PROCESSO 🚧)

Recuperação de senha

Interface gráfica (GUI)

Integração com banco de dados (MySQL, PostgreSQL)

Sistema de autenticação com tokens (JWT)

Criptografia mais robusta (bcrypt)

👨‍💻 Autor

Pedro Vieira
