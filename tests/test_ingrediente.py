import unittest
from models.models_bd import Ingrediente

class Test_Ingrediente(unittest.TestCase):
    def setUp(self):
        self.ingrediente1 = Ingrediente(id=1, precio=2000, calorias=100, nombre="Crema", inventario=1.0, es_vegetariano=0, tipo_ingrediente="Base")
        self.ingrediente2 = Ingrediente(id=1, precio=2000, calorias=100, nombre="Crema", inventario=1.0, es_vegetariano=1, tipo_ingrediente="Complemento")

    #Ingrediente1 es sano
    def test_ingrediente_es_sano(self):
        self.assertEqual(self.ingrediente2.es_sano(), 1)
    
    #Ingrediente2 no es sano
    def test_ingrediente_no_es_sano(self):
        self.assertEqual(self.ingrediente1.es_sano(), 0)

    #Ingrediente1 es de tipo Base abastecer
    def test_ingrediente_abastecer_base(self):
        self.ingrediente1.abastecer()
        self.assertEqual(self.ingrediente1.inventario, 6.0)

    #Ingrediente2 es de tipo Complemento abastecer
    def test_ingrediente_abastecer_complemento(self):
        self.ingrediente2.abastecer()
        self.assertEqual(self.ingrediente2.inventario, 11.0)

    #Ingrediente2 es de tipo Complemento renovar
    def test_ingrediente_renovar_complemento(self):
        self.ingrediente2.renovar_inventario()
        self.assertEqual(self.ingrediente2.inventario, 0.0)
        