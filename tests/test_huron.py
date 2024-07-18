import unittest
from models.huron import Huron

class Test_Huron(unittest.TestCase):

    def setUp(self):
        self.huron = Huron("Rayo", 5.5, 2, "Australia", 10.5) 

    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        self.assertEqual(self.huron.calcular_flete(), 57.75)