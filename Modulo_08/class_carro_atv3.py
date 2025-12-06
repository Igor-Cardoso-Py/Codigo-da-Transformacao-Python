class Carro:
    def _init_(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def _str_(self):
        return f"{self.marca} {self.modelo}"


class CarroEletrico(Carro):
    def _init_(self, marca, modelo, autonomia_bateria):
        super()._init_(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def _str_(self):
        return f"{self.marca} {self.modelo} - {self.autonomia_bateria} km de autonomia"


# Testando
c1 = Carro("Fiat", "Argo")
c2 = CarroEletrico("BYD", "Dolphin", 350)

print(c1)
print(c2)