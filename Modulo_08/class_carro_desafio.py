class Livro:
    def _init_(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def _str_(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} - {self.autor} ({status})"


class Biblioteca:
    def _init_(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def emprestar(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                return f"Você emprestou: {livro.titulo}"
        return "Livro indisponível ou não encontrado."

    def devolver(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and not livro.disponivel:
                livro.disponivel = True
                return f"Livro devolvido: {livro.titulo}"
        return "Este livro não estava emprestado."

    def listar_livros(self):
        return "\n".join(str(livro) for livro in self.livros)


# Testando
b = Biblioteca()

l1 = Livro("1984", "George Orwell")
l2 = Livro("Dom Casmurro", "Machado de Assis")

b.adicionar_livro(l1)
b.adicionar_livro(l2)

print(b.listar_livros())
print(b.emprestar("1984"))
print(b.listar_livros())
print(b.devolver("1984"))
print(b.listar_livros())