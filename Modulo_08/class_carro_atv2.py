class Carro:
    def _init_(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Carro: {self.marca} {self.modelo}"


class CarroEletrico(Carro):
    def _init_(self, marca, modelo, autonomia_bateria):
        super()._init_(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        return (f"Carro Elétrico: {self.marca} {self.modelo} | "
                f"Autonomia: {self.autonomia_bateria} km")


# Testando
carroE = CarroEletrico("Tesla", "Model 3", 450)
print(carroE.exibir_info())