import sqlite3

# Conexão
def conectar():
    return sqlite3.connect("tarefas.db")

# Criar tabela
def criar_tabela():
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL
        );
    """)
    con.commit()
    con.close()

# Adicionar tarefa
def adicionar_tarefa(desc):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO tarefas (descricao) VALUES (?)", (desc,))
    con.commit()
    con.close()
    print("Tarefa adicionada!")

# Listar tarefas
def listar_tarefas():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM tarefas")
    tarefas = cur.fetchall()
    con.close()
    return tarefas

# Excluir tarefa
def excluir_tarefa(id_tarefa):
    con = conectar()
    cur = con.cursor()
    cur.execute("DELETE FROM tarefas WHERE id=?", (id_tarefa,))
    con.commit()
    con.close()
    print("Tarefa excluída!")

# ---- Execução de exemplo ----
criar_tabela()
adicionar_tarefa("Estudar Python")
adicionar_tarefa("Ir para a academia")

print("Tarefas cadastradas:")
print(listar_tarefas())

excluir_tarefa(1)

print("Após excluir:")
print(listar_tarefas())