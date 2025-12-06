import unittest
from calculadora import Calculadora

class TestCalculadoraInvalidas(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if _name_ == '_main_':
    unittest.main()