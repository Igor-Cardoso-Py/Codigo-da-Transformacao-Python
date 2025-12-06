import sqlite3

def conectar():
    return sqlite3.connect("clientes.db")

# Inserir cliente
def inserir(nome, email):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
    con.commit()
    con.close()
    print("Cliente cadastrado!")

# Consultar todos
def consultar():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM clientes")
    dados = cur.fetchall()
    con.close()
    return dados

# Atualizar cliente
def atualizar(id_cliente, novo_nome, novo_email):
    con = conectar()
    cur = con.cursor()
    cur.execute("UPDATE clientes SET nome=?, email=? WHERE id=?", 
                (novo_nome, novo_email, id_cliente))
    con.commit()
    con.close()
    print("Cliente atualizado!")

# Deletar cliente
def deletar(id_cliente):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM clientes WHERE id=?", (id_cliente,))
    con.commit()
    con.close()
    print("Cliente removido!")


# Exemplos de uso:
inserir("Ana", "ana@gmail.com")
inserir("Carlos", "carlos@gmail.com")

print("Clientes cadastrados:")
print(consultar())

atualizar(1, "Ana Paula", "anapaula@gmail.com")
deletar(2)

print("Clientes após alterações:")
print(consultar())