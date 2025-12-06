def ler_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))

            if idade <= 0:
                raise ValueError("A idade deve ser um número positivo.")

            return idade

        except ValueError as erro:
            print(f"Erro: {erro}")

# Teste
idade = ler_idade()
print(f"Idade registrada com sucesso: {idade}")