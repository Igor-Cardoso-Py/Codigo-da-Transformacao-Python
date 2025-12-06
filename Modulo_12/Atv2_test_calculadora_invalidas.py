import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calc.somar(10, 5), 15)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(20, 4), 5)

if _name_ == '_main_':
    unittest.main()