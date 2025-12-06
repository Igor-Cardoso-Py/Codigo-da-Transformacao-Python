USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

def sistema_login():
    tentativas = 3

    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            print("Login realizado com sucesso!")
            return True
        else:
            tentativas -= 1
            print(f"Credenciais inválidas! Tentativas restantes: {tentativas}")

    print("Número de tentativas excedido. Acesso bloqueado.")
    return False

# Teste
sistema_login()