import sqlite3

# Conectar ao banco
con = sqlite3.connect("clientes.db")
cur = con.cursor()

# Criar tabela
cur.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
);
""")

con.commit()
con.close()

print("Tabela 'clientes' criada com sucesso!")