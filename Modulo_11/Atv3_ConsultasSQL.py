import sqlite3

def clientes_com_a():
    con = sqlite3.connect("clientes.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM clientes WHERE nome LIKE 'A%'")
    dados = cur.fetchall()
    con.close()
    return dados

print("Clientes cujo nome começa com 'A':")
print(clientes_com_a())