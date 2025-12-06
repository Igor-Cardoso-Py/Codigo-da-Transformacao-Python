import unittest
from soma import soma

class TestSoma(unittest.TestCase):

    def test_soma_simples(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -4), -5)

    def test_soma_float(self):
        self.assertAlmostEqual(soma(2.5, 3.1), 5.6)

if _name_ == '_main_':
    unittest.main()