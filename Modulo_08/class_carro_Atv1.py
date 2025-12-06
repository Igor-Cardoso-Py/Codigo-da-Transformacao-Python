class Carro:
    def _init_(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Carro: {self.marca} {self.modelo}"


# Testando
carro1 = Carro("Toyota", "Corolla")
print (carro1.exibir_info())