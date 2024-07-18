import unittest
from models.boa_constrictor import Boa_Constrictor

class Test_Boa(unittest.TestCase):

    def setUp(self):
        self.boa = Boa_Constrictor("Titan", 50.2, 3, "Brasil", 30.5)

    def test_hacer_sonido(self):
        self.assertEqual(self.boa.hacer_sonido(), "Tsss!")

    def test_calcular_flete(self):
        self.assertEqual(self.boa.calcular_flete(), 1531.1)
    
    def test_calcular_flete(self):
        self.boa.sumar_ratones_comidos(5)
        self.assertEqual(self.boa.obtener_ratones_comidos(), 5)
        self.boa.sumar_ratones_comidos(5)
        self.assertEqual(self.boa.obtener_ratones_comidos(), 10)
        