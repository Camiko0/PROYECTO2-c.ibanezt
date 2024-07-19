import unittest
from models.models_bd import Producto

class Test_Producto(unittest.TestCase):
    def setUp(self):
        self.producto1 = Producto(id=1, nombre="Helado de chocolate", precio_publico=12000, tipo_producto="Copa", tipo_vaso="Desechable")
        self.producto2 = Producto(id=1, nombre="Sorbete de coco", precio_publico=10000, tipo_producto="Malteada", volumen=20.5)

    #Producto1 es de tipo Copa calcular calorias
    def test_calcular_calorias_copa(self):
        self.assertEqual(self.producto1.calcular_calorias(self.producto1.tipo_producto, [1000, 950, 850]), 2660.0)

    #Producto2 es de tipo Malteada calcular calorias
    def test_calcular_calorias_malteada(self):
        self.assertEqual(self.producto2.calcular_calorias(self.producto2.tipo_producto, [1000, 950, 850]), 3000.0)

    #Producto1 es de tipo Copa calcular costo
    def test_calcular_costo_copa(self):
        self.assertEqual(self.producto1.calcular_costo(self.producto1.tipo_producto, [{"precio": 1000}, {"precio": 950}, {"precio": 850}]), 2800)

    #Producto1 es de tipo Copa calcular rentabilidad
    def test_calcular_rentabilidad_copa(self):
        self.assertEqual(self.producto1.calcular_rentabilidad(self.producto1.tipo_producto, self.producto1.precio_publico,
                                                       [{"precio": 1000}, {"precio": 950}, {"precio": 850}]), 9200)
    #Producto1 es de tipo Copa calcular rentabilidad
    def test_calcular_producto_mas_rentable(self):
        rentabilidad1 = self.producto1.calcular_rentabilidad(self.producto1.tipo_producto, self.producto1.precio_publico,
                                                       [{"precio": 1000}, {"precio": 950}, {"precio": 850}])
        rentabilidad2 = self.producto2.calcular_rentabilidad(self.producto2.tipo_producto, self.producto2.precio_publico,
                                                       [{"precio": 1000}, {"precio": 950}, {"precio": 850}])
        self.assertEqual(rentabilidad1 > rentabilidad2, True)

        